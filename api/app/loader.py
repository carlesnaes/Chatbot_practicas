import os
import re
from pathlib import Path
from typing import List, Tuple, Optional

import fitz  # PyMuPDF
import pdfplumber
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

# ============================================================
# Rutas robustas
# ============================================================
DATA_DIR = Path(os.getenv("DATA_DIR", Path(__file__).resolve().parent / "Datos")).resolve()


def _diagnostico_rutas(objetivo: Path) -> str:
    """Mensaje útil cuando un archivo no se encuentra."""
    try:
        contenido = [p.name for p in (DATA_DIR.iterdir() if DATA_DIR.exists() else [])]
    except Exception:
        contenido = []
    return (
        f"\n  • Buscado: {objetivo}\n"
        f"  • DATA_DIR: {DATA_DIR}\n"
        f"  • CWD: {os.getcwd()}\n"
        f"  • Contenido de DATA_DIR: {contenido}"
    )


def _resolve_path(path_like: str | Path) -> Path:
    """
    Resuelve una ruta de forma tolerante:
      1) Si es absoluta y existe → OK
      2) Si es relativa y existe desde CWD → OK
      3) Si no existe, se intenta bajo DATA_DIR manteniendo subrutas
      4) Si sigue sin existir, se prueba DATA_DIR / nombre_archivo
    """
    p = Path(path_like)

    # 1) Absoluta existente
    if p.is_absolute() and p.exists():
        return p

    # 2) Relativa existente desde CWD
    if not p.is_absolute() and p.exists():
        return p.resolve()

    # 3) Probar bajo DATA_DIR conservando subrutas
    candidate = (DATA_DIR / p).resolve()
    if candidate.exists():
        return candidate

    # 4) Último intento: DATA_DIR / nombre
    candidate2 = (DATA_DIR / p.name).resolve()
    if candidate2.exists():
        return candidate2

    # No existe: devolvemos la ruta “mejor suposición”
    return candidate


# ============================================================
# Utilidades de texto/PDF
# ============================================================

def limpiar_texto(texto: str) -> str:
    """Limpia saltos y espacios múltiples."""
    return re.sub(r"\s+", " ", texto).strip()


def extraer_texto_pdf(ruta_pdf: str | Path) -> str:
    """
    Extrae texto del PDF con PyMuPDF y anota URLs si la caja del span
    intersecta la caja de un enlace (tu lógica original).
    """
    ruta_resuelta = _resolve_path(ruta_pdf)
    print("La ruta actual es:", os.getcwd())
    if not ruta_resuelta.exists():
        raise FileNotFoundError(
            " No se encontró el PDF para extraer texto." + _diagnostico_rutas(ruta_resuelta)
        )

    texto = ""
    with fitz.open(str(ruta_resuelta)) as doc:
        for page in doc:
            links = page.get_links()  # cache enlaces por página
            link_rects = [(fitz.Rect(l["from"]), l.get("uri", "")) for l in links if "from" in l]
            blocks = page.get_text("dict")["blocks"]
            for block in blocks:
                if "lines" in block:
                    for line in block["lines"]:
                        for span in line["spans"]:
                            span_text = span["text"]
                            span_rect = fitz.Rect(span["bbox"])
                            # ¿interseca con algún enlace?
                            for lrect, uri in link_rects:
                                if uri and span_rect.intersects(lrect):
                                    span_text += f" (url: {uri})"
                                    break
                            texto += span_text
                        texto += "\n"
            texto += "\n"

    return texto


# ============================================================
# API principal 
# ============================================================

def cargar_documentos_y_tabla(
    archivos_pdf: List[Tuple[str, str]],
    ruta_tabla_pdf: Optional[str],
    role: str,
    school: str = "ALL",
    solo_tabla: bool = False
) -> List[Document]:
    """
    Carga documentos PDF y/o extrae la tabla de créditos-horas para generar objetos Document.

    - archivos_pdf: lista de (ruta_pdf, nombre_txt_para_metadata) o rutas simples
    - ruta_tabla_pdf: ruta del PDF que contiene la tabla de créditos-horas
    - role: 'estudiante' o 'empresa'
    - school: nombre de la escuela o 'ALL'
    - solo_tabla: si True, solo procesa la tabla (no los textos PDF)
    """
    docs: List[Document] = []
    text_chunks: List[Document] = []   
    tabla_docs: List[Document] = []    

    # =====================================================
    #  1) Extracción de texto de PDFs → Document
    # =====================================================
    if not solo_tabla and archivos_pdf:
        for item in archivos_pdf:
            try:
                if isinstance(item, (list, tuple)) and len(item) == 2:
                    ruta_pdf, nombre_txt = item
                elif isinstance(item, str):
                    ruta_pdf, nombre_txt = item, os.path.basename(item)
                else:
                    raise ValueError(f"Formato inválido en archivos_pdf: {item}")

                texto = extraer_texto_pdf(ruta_pdf)
                if texto.strip():
                    docs.append(
                        Document(
                            page_content=texto,
                            metadata={"source": nombre_txt, "role": role, "school": school}
                        )
                    )
            except Exception as e:
                print(f" Warning: no se pudo procesar {item}: {e}")

        if docs:
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200,
                separators=["\n\n", "\n", " ", ""]
            )
            text_chunks = splitter.split_documents(docs)

    # =====================================================
    #  2) Extracción de tabla créditos-horas → Document
    # =====================================================
    if ruta_tabla_pdf:
        try:
            import pdfplumber
            filas = []
            with pdfplumber.open(ruta_tabla_pdf) as pdf:
                for page in pdf.pages:
                    tables = page.extract_tables() or []
                    for table in tables:
                        for row in table:
                            filas.append(row)

            titulacion_temp = ""
            for fila in filas[1:]:
                fila = [(c or "").replace("\n", " ").strip() for c in fila if c]

                if not fila:
                    continue

                # Corregir filas con columnas desplazadas
                if len(fila) >= 4 and not fila[0]:
                    fila = fila[1:]

                if len(fila) == 1:
                    titulacion_temp = f"{titulacion_temp} {fila[0]}".strip()
                    continue

                if len(fila) == 2:
                    titulacion = titulacion_temp or "Titulación desconocida"
                    curriculares, extracurriculares = fila
                    titulacion_temp = ""
                elif len(fila) >= 3:
                    titulacion, curriculares, extracurriculares = fila[:3]
                else:
                    continue

                contenido = (
                    f"Información oficial sobre las prácticas externas en la titulación de {titulacion}, "
                    f"según la normativa de la Universitat Politècnica de València (UPV). "
                    f"Los estudiantes matriculados pueden realizar prácticas externas en "
                    f"{'modalidad de prácticas extracurriculares' if 'doble grado' in titulacion.lower() else 'dos modalidades: prácticas curriculares y extracurriculares'}. "
                    f"{'' if 'doble grado' in titulacion.lower() else f'Las prácticas curriculares están limitadas a {curriculares}, computando créditos ECTS. '} "
                    f"Las extracurriculares {'son voluntarias' if 'doble grado' in titulacion.lower() else 'no son curriculares y son voluntarias'}, "
                    f"con un máximo de {extracurriculares}. "
                    f"Esta información corresponde a la escuela {school}."
                )

                tabla_docs.append(
                    Document(
                        page_content=contenido,
                        metadata={"source": "tabla créditos-horas", "role": role, "school": school}
                    )
                )

        except Exception as e:
            print(f" Error al procesar la tabla {ruta_tabla_pdf}: {e}")

    # =====================================================
    #  3) Combinar resultados
    # =====================================================
    return text_chunks + tabla_docs
