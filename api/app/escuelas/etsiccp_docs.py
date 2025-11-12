from langchain.schema import Document
from app.loader import cargar_documentos_y_tabla
from pathlib import Path
import os

def cargar_docs_etsiccp():
    """Carga los documentos manuales de la ETSICCP (Escuela Técnica Superior de Ingenieros de Caminos, Canales y Puertos-UPV)."""
    try:
        DATA_DIR = Path(os.getenv("DATA_DIR", Path(__file__).resolve().parents[1] / "Datos")).resolve()
        RUTA_CAMINOS = str(DATA_DIR / "normativa_caminos.pdf")

        # Cargar la normativa en PDF (si está disponible)
        overlay_caminos = cargar_documentos_y_tabla(
            archivos_pdf=[RUTA_CAMINOS],
            ruta_tabla_pdf=None,
            role="estudiante",
            school="ETSICCP",
            solo_tabla=False
        )

        print("ETSICCP cargado correctamente.")
        manual_etsiccp = [
            # ------------------ GRADOS ------------------
            Document(
                page_content=(
                    "En el Grado en Ingeniería Civil (código 213, ETSICCP-UPV), los estudiantes pueden realizar hasta "
                    "1.800 horas de prácticas extracurriculares y 18 créditos ECTS de prácticas curriculares "
                    "(450 horas)."
                ),
                metadata={"source": "manual", "categoria": "practicas_grado_ingenieria_civil", "role": "estudiante", "school": "ETSICCP"}
            ),
            Document(
                page_content=(
                    "En el Grado en Ingeniería Civil (código 173, a extinguir, ETSICCP-UPV), los estudiantes pueden realizar hasta "
                    "1.800 horas de prácticas extracurriculares y 4,5 créditos ECTS de prácticas curriculares (112,5 horas)."
                ),
                metadata={"source": "manual", "categoria": "practicas_grado_ingenieria_civil_extinguido", "role": "estudiante", "school": "ETSICCP"}
            ),
            Document(
                page_content=(
                    "En el Grado en Ingeniería de Obras Públicas (código 168, a extinguir, ETSICCP-UPV), los estudiantes pueden realizar hasta "
                    "1.800 horas de prácticas extracurriculares y 6 créditos ECTS de prácticas curriculares (150 horas)."
                ),
                metadata={"source": "manual", "categoria": "practicas_grado_obras_publicas", "role": "estudiante", "school": "ETSICCP"}
            ),
            Document(
                page_content=(
                    "En el Grado en Gestión del Transporte y Logística (código 211, ETSICCP-UPV), los estudiantes pueden realizar hasta "
                    "1.800 horas de prácticas extracurriculares y 18 créditos ECTS de prácticas curriculares (450 horas)."
                ),
                metadata={"source": "manual", "categoria": "practicas_grado_transporte_logistica", "role": "estudiante", "school": "ETSICCP"}
            ),

            # ------------------ DOBLE GRADO ------------------
            Document(
                page_content=(
                    "En el Doble Grado en Matemáticas e Ingeniería Civil (código 217, ETSICCP-UPV), "
                    "los estudiantes pueden realizar hasta 2.700 horas de prácticas extracurriculares. "
                    "No incluye prácticas curriculares en el plan de estudios."
                ),
                metadata={"source": "manual", "categoria": "practicas_doble_grado_matematicas_civil", "role": "estudiante", "school": "ETSICCP"}
            ),

            # ------------------ MÁSTERES ------------------
            Document(
                page_content=(
                    "En el Máster Universitario en Ingeniería de Caminos, Canales y Puertos (MUICCP, código 2323, ETSICCP-UPV), "
                    "los estudiantes pueden realizar hasta 1.200 horas de prácticas extracurriculares y 18 créditos ECTS de prácticas curriculares (450 horas)."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_muiccp_2323", "role": "estudiante", "school": "ETSICCP"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Ingeniería de Caminos, Canales y Puertos (MUICCP, código 2236, a extinguir, ETSICCP-UPV), "
                    "los estudiantes pueden realizar hasta 1.200 horas de prácticas extracurriculares y 4,5 créditos ECTS de prácticas curriculares (112,5 horas)."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_muiccp_2236", "role": "estudiante", "school": "ETSICCP"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Ingeniería de Caminos, Canales y Puertos (MUICCP, código 2257, a extinguir, ETSICCP-UPV), "
                    "los estudiantes pueden realizar hasta 1.200 horas de prácticas extracurriculares y 4,5 créditos ECTS de prácticas curriculares (112,5 horas)."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_muiccp_2257", "role": "estudiante", "school": "ETSICCP"}
            ),
            Document(
                page_content=(
                    "En el Máster en Planificación y Gestión en Ingeniería Civil (código 2305, ETSICCP-UPV), "
                    "los estudiantes pueden realizar hasta 750 horas de prácticas extracurriculares y 15 créditos ECTS de prácticas curriculares (375 horas)."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_planificacion_gestion_civil", "role": "estudiante", "school": "ETSICCP"}
            ),
            Document(
                page_content=(
                    "En el Máster en Transporte, Territorio y Urbanismo (código 2277, ETSICCP-UPV), "
                    "los estudiantes pueden realizar hasta 750 horas de prácticas extracurriculares. "
                    "No incluye prácticas curriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_transporte_urbanismo", "role": "estudiante", "school": "ETSICCP"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Ingeniería Ambiental (código 2301, ETSICCP-UPV), "
                    "los estudiantes pueden realizar hasta 900 horas de prácticas extracurriculares y 6 créditos ECTS de prácticas curriculares (150 horas)."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_ingenieria_ambiental", "role": "estudiante", "school": "ETSICCP"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Ingeniería Estructural y Geotécnica (código 2313, ETSICCP-UPV), "
                    "los estudiantes pueden realizar hasta 900 horas de prácticas extracurriculares y 6 créditos ECTS de prácticas curriculares (150 horas)."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_ingenieria_estructural", "role": "estudiante", "school": "ETSICCP"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Prevención de Riesgos Laborales (ETSICCP-UPV), "
                    "los estudiantes pueden realizar hasta 900 horas de prácticas extracurriculares y 9 créditos ECTS de prácticas curriculares (225 horas)."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_prevencion_riesgos", "role": "estudiante", "school": "ETSICCP"}
            ),
        ]
        overlay_caminos= overlay_caminos + manual_etsiccp
        return overlay_caminos

    except Exception as e:
        print(f"⚠️ ETSICCP no cargada: {e}")
        return []
