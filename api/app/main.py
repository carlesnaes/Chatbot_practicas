import os
import time
import asyncio
import html, re
from fastapi import FastAPI, Depends, Query, HTTPException, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from sse_starlette.sse import EventSourceResponse
from fastapi.staticfiles import StaticFiles
from loguru import logger
from pydantic import BaseModel, constr, Field, validator
from sqlalchemy.future import select


from collections import Counter
from fastapi.responses import HTMLResponse, JSONResponse, Response
from sqlalchemy.future import select
from jinja2 import Template

from fastapi import Request


import subprocess
from openai import OpenAI



from app.adapter import init_rag, chat_with_rag
from app.db import AsyncSessionLocal, Feedback, Conversation, init_db
from app.sanitizer import sanitize_html
from app.rag_chain import get_vectorstore

from datetime import datetime, timedelta
from sqlalchemy import select, func


# =========================================================
# CONFIG
# =========================================================
ADMIN_KEY = os.getenv("ADMIN_KEY")
if not ADMIN_KEY:
    raise RuntimeError(" Falta definir ADMIN_KEY a las variables de entorno.")
SESSION_LIMIT = 20            # máximo 20 mensajes
WINDOW_MIN = 30               # en 30 minutos

# =========================================================
# VALIDACIÓN Y SANITIZACIÓN INPUT
# =========================================================
class ChatInput(BaseModel):
    message: constr(min_length=1, max_length=1000)
    role: str = Field(..., pattern="^(estudiante|empresa)$")
    school: str | None = "ALL"
    session_id: str | None = None



    @validator("message")
    def sanitize_message(cls, v):
            return sanitize_html(v)




# =========================================================
# FASTAPI APP
# =========================================================
app = FastAPI(title="RAG Chat API")

# CORS (solo si hay dominios definidos)
origins = [o.strip() for o in os.getenv("ALLOWED_ORIGINS", "").split(",") if o.strip()]
if origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


# =========================================================
# EVENTOS DE INICIO
# =========================================================
@app.on_event("startup")
async def startup_event():
    await init_rag()   # inicializa FAISS / embeddings
    await init_db()    # inicializa BD SQLite/SQLAlchemy
    get_vectorstore()  # ← bloquea hasta cargar/crear; queda cacheado

    logger.info(" API iniciada correctamente (RAG + DB lista)")


# =========================================================
# ENDPOINTS
# =========================================================
@app.get("/health")
def health():
    return {"status": "ok"}



@app.middleware("http")
async def add_csp_header(request, call_next):
    response = await call_next(request)
    path = request.url.path

    # Política más flexible solo para panel admin
    if path.startswith("/admin"):
        response.headers["Content-Security-Policy"] = (
            "default-src 'self'; "
            "script-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net; "
            "style-src 'self' 'unsafe-inline'; "
            "img-src 'self' data:; "
            "object-src 'none'; "
            "base-uri 'self'; "
            "frame-ancestors 'none';"
        )
    else:
        # Política estricta para el resto de la web
        response.headers["Content-Security-Policy"] = (
            "default-src 'self'; "
            "script-src 'self'; "
            "style-src 'self'; "
            "img-src 'self' data:; "
            "object-src 'none'; "
            "base-uri 'self'; "
            "frame-ancestors 'none';"
        )

    #  Cabeceras de seguridad adicionales
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Referrer-Policy"] = "no-referrer"
    response.headers["X-Content-Type-Options"] = "nosniff"

    return response



@app.post("/chat")
async def chat(body: ChatInput, request: Request):
    """
    Endpoint principal del chatbot RAG (sin memoria)
    """

    query = body.message
    role = body.role
    school = (body.school or "ALL").upper()
    sid = body.session_id or f"anon_{role}_{school}"

    # Las empresas siempre van a ALL
    if role == "empresa":
        school = "ALL"

    # -------------------------------
    #  RATE LIMIT POR SESIÓN
    # -------------------------------
    try:
        async with AsyncSessionLocal() as db:

            window_start = datetime.utcnow() - timedelta(minutes=WINDOW_MIN)

            q = select(func.count()).select_from(Conversation).where(
                Conversation.user_id == request.headers.get("X-User-ID"),
                Conversation.created_at >= window_start
            )


            result = await db.execute(q)
            session_count = result.scalar()

            if session_count >= SESSION_LIMIT:
                return {
                    "error": f"Has alcanzado el límite de {SESSION_LIMIT} mensajes por sesión en {WINDOW_MIN} minutos.",
                    "retry_after_minutes": WINDOW_MIN
                }
    except Exception as e:
        logger.error(f"❌ Error aplicando rate limit: {e}")
        raise HTTPException(status_code=500, detail="Error interno en el sistema de límites")

    # -------------------------------
    #  CHAT RAG
    # -------------------------------
    try:
        answer, sources = await chat_with_rag(query, role, school, sid)

    except Exception as e:
        logger.error(f"❌ Error durante chat_with_rag: {e}")
        raise HTTPException(status_code=500, detail="Error interno en el motor RAG")

    # -------------------------------
    #  GUARDAR EN BD
    # -------------------------------
    try:
        async with AsyncSessionLocal() as db:
            record = Conversation(
                session_id=sid,
                user_id=request.headers.get("X-User-ID"),
                role=role,
                question=sanitize_html(query),
                answer=sanitize_html(answer),
                school=school,
            )
            db.add(record)
            await db.commit()

    except Exception as e:
        logger.error(f"❌ Error guardando la conversación en BD: {e}")
        raise HTTPException(status_code=500, detail="Error guardando la conversación")

    # -------------------------------
    #  RESPUESTA AL CLIENTE
    # -------------------------------
    return {"answer": answer, "sources": sources}


@app.post("/feedback")
async def feedback_handler(body: dict,request: Request):
    """Guarda el feedback enviado desde el frontend."""
    session_id = body.get("session_id")
    role = body.get("role")
    question = sanitize_html(body.get("question") or body.get("message"))
    answer = sanitize_html(body.get("answer", ""))
    feedback = body.get("feedback")

    if not question or feedback not in ("positive", "negative"):
        raise HTTPException(status_code=400, detail="Campos inválidos o incompletos")

    async with AsyncSessionLocal() as db:
        entry = Feedback(
            session_id=session_id,
            user_id=request.headers.get("X-User-ID"),
            role=role,
            question=question,
            answer=answer,
            feedback=feedback,
        )
        db.add(entry)
        await db.commit()

    return {"ok": True, "status": "feedback guardado"}




@app.get("/admin/conversaciones", response_class=HTMLResponse)
async def admin_conversaciones(key: str):
    if key != os.getenv("ADMIN_KEY", "upv2025"):
        return HTMLResponse("<h3>Acceso no autorizado</h3>", status_code=403)

    async with AsyncSessionLocal() as session:
        #  Obtener todas las conversaciones
        result_conv = await session.execute(
            select(Conversation).order_by(Conversation.created_at.desc())
        )
        conversaciones = result_conv.scalars().all()

        #  Obtener todos los feedbacks (para vincularlos por session_id + question)
        result_fb = await session.execute(select(Feedback))
        feedbacks = result_fb.scalars().all()

        #  Crear diccionario para búsqueda rápida
        feedback_map = {}
        for fb in feedbacks:
            key = (fb.session_id or "") + "|" + (fb.question or "")
            feedback_map[key] = fb.feedback  # "positive" o "negative"

        # Enriquecer las conversaciones con el feedback correspondiente
        conv_rows = []
        for c in conversaciones:
            key = (c.session_id or "") + "|" + (c.question or "")
            fb = feedback_map.get(key)
            if fb == "positive":
                fb_symbol = "👍"
            elif fb == "negative":
                fb_symbol = "👎"
            else:
                fb_symbol = "—"
            conv_rows.append((c, fb_symbol))

    # Renderizar HTML
    html_template = """
    <html>
    <head>
        <meta charset="utf-8">
        <title>Panel Conversaciones</title>
        <style>
            body { font-family: Arial, sans-serif; background:#f8f9fa; padding:20px; }
            table { border-collapse: collapse; width: 100%; background:white; box-shadow:0 2px 4px rgba(0,0,0,0.1); }
            th, td { border:1px solid #ddd; padding:8px; }
            th { background:#343a40; color:white; text-align:left; }
            tr:nth-child(even){background:#f2f2f2;}
            h1 { color:#343a40; }
            .timestamp { color:#666; font-size:0.9em; }
            .feedback-col { text-align:center; font-size:1.3em; }
        </style>
    </head>
    <body>
        <h1> Conversaciones registradas</h1>
        <table>
            <tr>
                <th>Fecha</th>
                <th>User ID</th>           
                <th>Sesión</th>
                <th>Rol</th>
                <th>Escuela</th>
                <th>Pregunta</th>
                <th>Feedback</th>
            </tr>
            {% for c, fb in conv_rows %}
            <tr>
                <td class="timestamp">{{ c.created_at.strftime("%d/%m/%Y %H:%M") }}</td>
                <td>{{ c.user_id }}</td>        
                <td>{{ c.session_id }}</td>
                <td>{{ c.role }}</td>
                <td>{{ c.school }}</td>
                <td>{{ c.question[:100] }}</td>
                <td class="feedback-col">{{ fb }}</td>
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    """
    template = Template(html_template)
    return HTMLResponse(template.render(conv_rows=conv_rows))


@app.get("/admin/estadisticas", response_class=HTMLResponse)
async def admin_estadisticas(key: str):
    if key != os.getenv("ADMIN_KEY", "upv2025"):
        return HTMLResponse("<h3>Acceso no autorizado</h3>", status_code=403)

    async with AsyncSessionLocal() as session:
        # Conversaciones por día
        res_conv = await session.execute(select(Conversation.created_at))
        fechas = [c[0].strftime("%Y-%m-%d") for c in res_conv.all()]

        # Feedback
        res_fb = await session.execute(select(Feedback.feedback))
        feedbacks = [f[0] for f in res_fb.all()]

        # Escuela y Rol
        res_school = await session.execute(select(Conversation.school))
        schools = [s[0] or "Desconocida" for s in res_school.all()]

        res_role = await session.execute(select(Conversation.role))
        roles = [r[0] for r in res_role.all()]

    conv_por_dia = Counter(fechas)
    feedback_counts = Counter(feedbacks)
    school_counts = Counter(schools)
    role_counts = Counter(roles)

    # Para asegurar que Chart.js siempre tiene algo que graficar
    def safe(counter):
        if not counter:
            return ["Sin datos"], [0]
        return list(counter.keys()), list(counter.values())

    days_labels, days_values = safe(conv_por_dia)
    fb_labels, fb_values = ["Positivas", "Negativas"], [
        feedback_counts.get("positive", 0),
        feedback_counts.get("negative", 0)
    ]
    school_labels, school_values = safe(school_counts)
    role_labels, role_values = safe(role_counts)

    html = f"""
    <html>
    <head>
        <meta charset="utf-8">
        <title>Panel de Estadísticas</title>
        <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
        <style>
            :root {{
                --page-max: 1200px;
                --gap: 24px;
                --card-h: 320px;
            }}

            body {{
                font-family: Arial, sans-serif;
                background: #f8f9fa;
                margin: 0;
            }}

            .page {{
                max-width: var(--page-max);
                margin: 0 auto;
                padding: 30px 16px;
            }}

            h1 {{
                color: #343a40;
                display: flex;
                align-items: center;
                gap: 12px;
                margin: 0 0 16px 0;
            }}
            h1::before {{
                content: "📊";
                font-size: 1.4em;
            }}

            .charts {{
                display: grid;
                grid-template-columns: repeat(2, minmax(340px, 1fr));
                gap: var(--gap);
                align-items: stretch;
                justify-items: stretch;
                margin-top: 16px;
            }}

            .chart-card {{
                background: #fff;
                border-radius: 12px;
                box-shadow: 0 2px 6px rgba(0,0,0,0.08);
                padding: 12px;
                height: var(--card-h);
                display: flex;
            }}

            /* El canvas ocupa toda la tarjeta */
            .chart-card canvas {{
                width: 100% !important;
                height: 100% !important;
                display: block;
            }}

            @media (max-width: 980px) {{
                .charts {{
                grid-template-columns: 1fr;
                }}
            }}
            </style>



    </head>
    <body>
        <div class="page">
            <h1>Panel de Estadísticas</h1>

            <div class="charts">
                <div class="chart-card"><canvas id="chart1"></canvas></div>
                <div class="chart-card"><canvas id="chart2"></canvas></div>
                <div class="chart-card"><canvas id="chart3"></canvas></div>
                <div class="chart-card"><canvas id="chart4"></canvas></div>
            </div>
            </div>


        <script>
            const chartData = {{
                days: {{ labels: {days_labels}, values: {days_values} }},
                feedback: {{ labels: {fb_labels}, values: {fb_values} }},
                school: {{ labels: {school_labels}, values: {school_values} }},
                role: {{ labels: {role_labels}, values: {role_values} }}
            }};

            const createChart = (id, type, label, data, colors) => {{
                new Chart(document.getElementById(id).getContext('2d'), {{
                    type: type,
                    data: {{
                    labels: data.labels,
                    datasets: [{{
                        label: label,
                        data: data.values,
                        backgroundColor: colors
                    }}]
                    }},
                    options: {{
                    responsive: true,
                    maintainAspectRatio: false,   // <— clave para respetar la altura de la tarjeta
                    layout: {{ padding: 8 }},
                    plugins: {{
                        legend: {{ display: true, position: 'top' }},
                        title: {{ display: true, text: label }}
                    }},
                    scales: type === 'bar' ? {{
                        y: {{ beginAtZero: true, ticks: {{ stepSize: 1 }} }}
                    }} : {{}}
                    }}
                }});
            }};


            createChart("chart1", "bar", "Conversaciones por día", chartData.days, "#007bff");
            createChart("chart2", "doughnut", "Feedback recibido", chartData.feedback, ["#28a745", "#dc3545"]);
            createChart("chart3", "pie", "Distribución por escuela", chartData.school, ["#007bff","#17a2b8","#ffc107","#6610f2","#e83e8c"]);
            createChart("chart4", "doughnut", "Distribución por rol", chartData.role, ["#20c997","#fd7e14"]);
        </script>
    </body>
    </html>
    """
    return HTMLResponse(html)


@app.get("/chat/stream")
async def chat_stream(
    session_id: str = Query(...),
    role: str = Query("estudiante"),
    q: str = Query(...),
):
    """Streaming token a token (efecto escritura en tiempo real)."""
    try:
        answer, sources = await chat_with_rag(q, role, "ALL")
    except Exception as e:
        logger.error(f" Error en streaming RAG: {e}")
        raise HTTPException(status_code=500, detail="Error interno en el motor RAG")

    async def event_gen():
        for token in answer.split():
            yield f"event: token\ndata: {token}\n\n"
            await asyncio.sleep(0.03)
        yield 'event: done\ndata: {"ok": true}\n\n'

    return EventSourceResponse(event_gen(), media_type="text/event-stream")


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL", "https://api.poligpt.upv.es"),
)
# === ASR config por entorno ===
ASR_MODEL = os.getenv("ASR_MODEL", "whisper-1")
ASR_BASE = os.getenv("OPENAI_ASR_BASE_URL", "https://api.openai.com/v1")
ASR_KEY  = os.getenv("OPENAI_ASR_API_KEY") 

# Cliente ASR separado del de chat
asr_client = OpenAI(api_key=ASR_KEY, base_url=ASR_BASE)

@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    # rutas temporales
    in_path  = f"/tmp/{file.filename}"
    out_path = in_path.rsplit(".", 1)[0] + ".wav"

    try:
        # Guardar entrada
        with open(in_path, "wb") as f:
            f.write(await file.read())

        # Convertir a WAV mono 16 kHz (lo que mejor traga whisper/4o-mini-transcribe)
        subprocess.run(
            ["ffmpeg", "-y", "-i", in_path, "-ac", "1", "-ar", "16000", out_path],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

        # Transcribir
        with open(out_path, "rb") as audio_f:
            tx = asr_client.audio.transcriptions.create(
                model=ASR_MODEL,   # "whisper-1" o "gpt-4o-mini-transcribe"
                file=audio_f,
                # response_format="json",  # por defecto ya devuelve .text; descomenta si quieres JSON explícito
            )

        return {"text": tx.text}

    except subprocess.CalledProcessError:
        raise HTTPException(status_code=500, detail="Error al convertir el audio con ffmpeg.")
    except Exception as e:
        # errores típicos: 401 (clave sin acceso), 404 (endpoint no soporta audio), 415 (formato)
        raise HTTPException(status_code=500, detail=f"Error al transcribir audio: {e}")
    finally:
        # Limpieza
        try:
            if os.path.exists(in_path): os.remove(in_path)
            if os.path.exists(out_path): os.remove(out_path)
        except Exception:
            pass
# =========================================================
# ARCHIVOS ESTÁTICOS (frontend)
# =========================================================
app.mount(
    "/static",
    StaticFiles(directory=os.path.join(os.path.dirname(__file__), "static")),
    name="static",
)
