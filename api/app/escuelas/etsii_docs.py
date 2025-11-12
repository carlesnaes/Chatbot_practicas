from langchain.schema import Document

def cargar_docs_etsii():
    """Carga los documentos manuales de la ETSII (Ingeniería Industrial-UPV)."""
    try:
        manual_etsii = [
            # ------------------ MÁSTERES ------------------
            Document(
                page_content=(
                    "En el Máster Universitario en Dirección y Gestión de Proyectos (72 ECTS, código 2250), "
                    "los estudiantes pueden realizar un máximo de 720 horas de prácticas extracurriculares "
                    "y 125 horas de prácticas curriculares (5 ECTS)."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_gestion_proyectos_72", "role": "estudiante", "school": "ETSII"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Dirección y Gestión de Proyectos (60 ECTS, código 2343), "
                    "los estudiantes pueden realizar un máximo de 600 horas de prácticas extracurriculares "
                    "y 50 horas de prácticas curriculares (2 ECTS)."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_gestion_proyectos_60", "role": "estudiante", "school": "ETSII"}
            ),
            Document(
                page_content=(
                    "En el Máster en Ingeniería Avanzada de Producción, Logística y Cadena de Suministro, "
                    "los estudiantes pueden realizar hasta 600 horas de prácticas extracurriculares. "
                    "No incluye prácticas curriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_logistica", "role": "estudiante", "school": "ETSII"}
            ),
            Document(
                page_content=(
                    "En el Máster en Tecnología Energética para el Desarrollo Sostenible, "
                    "los estudiantes pueden realizar hasta 900 horas de prácticas extracurriculares "
                    "y 225 horas de prácticas curriculares (9 ECTS)."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_energetica_sostenible", "role": "estudiante", "school": "ETSII"}
            ),
            Document(
                page_content=(
                    "En el Máster en Construcción e Instalaciones Industriales, "
                    "los estudiantes pueden realizar hasta 900 horas de prácticas extracurriculares. "
                    "No incluye prácticas curriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_construccion", "role": "estudiante", "school": "ETSII"}
            ),
            Document(
                page_content=(
                    "En el Máster en Seguridad Industrial, los estudiantes pueden realizar hasta "
                    "600 horas de prácticas extracurriculares y 225 horas de prácticas curriculares (9 ECTS)."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_seguridad_industrial", "role": "estudiante", "school": "ETSII"}
            ),
            Document(
                page_content=(
                    "En el Máster en Automatización e Informática Industrial, los estudiantes pueden realizar hasta "
                    "600 horas de prácticas extracurriculares. No incluye prácticas curriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_automatizacion", "role": "estudiante", "school": "ETSII"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Ingeniería Mecánica, los estudiantes pueden realizar hasta "
                    "900 horas de prácticas extracurriculares y 375 horas de prácticas curriculares (15 ECTS)."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_mecanica", "role": "estudiante", "school": "ETSII"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Ingeniería Hidráulica y Medio Ambiente, los estudiantes pueden realizar hasta "
                    "900 horas de prácticas extracurriculares y 375 horas de prácticas curriculares (15 ECTS)."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_hidraulica", "role": "estudiante", "school": "ETSII"}
            ),
            Document(
                page_content=(
                    "En el Máster en Seguridad Nuclear y Protección Radiológica, los estudiantes pueden realizar hasta "
                    "600 horas de prácticas extracurriculares y 112,5 horas de prácticas curriculares (4,5 ECTS)."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_seguridad_nuclear", "role": "estudiante", "school": "ETSII"}
            ),

            # ------------------ GRADOS ------------------
            Document(
                page_content=(
                    "En el Grado en Ingeniería de Tecnologías Industriales, los estudiantes pueden realizar hasta "
                    "1.800 horas de prácticas extracurriculares y 337,5 horas de prácticas curriculares (13,5 ECTS)."
                ),
                metadata={"source": "manual", "categoria": "practicas_grado_tecnologias_industriales", "role": "estudiante", "school": "ETSII"}
            ),
            Document(
                page_content=(
                    "En el Grado en Ingeniería de Organización Industrial, los estudiantes pueden realizar hasta "
                    "1.800 horas de prácticas extracurriculares y 262,5 horas de prácticas curriculares (10,5 ECTS)."
                ),
                metadata={"source": "manual", "categoria": "practicas_grado_organizacion_industrial", "role": "estudiante", "school": "ETSII"}
            ),
            Document(
                page_content=(
                    "En el Grado en Ingeniería Química, los estudiantes pueden realizar hasta "
                    "1.800 horas de prácticas extracurriculares y 450 horas de prácticas curriculares (18 ECTS)."
                ),
                metadata={"source": "manual", "categoria": "practicas_grado_quimica", "role": "estudiante", "school": "ETSII"}
            ),
            Document(
                page_content=(
                    "En el Grado en Ingeniería de la Energía, los estudiantes pueden realizar hasta "
                    "1.800 horas de prácticas extracurriculares y 450 horas de prácticas curriculares (18 ECTS)."
                ),
                metadata={"source": "manual", "categoria": "practicas_grado_energia", "role": "estudiante", "school": "ETSII"}
            ),
            Document(
                page_content=(
                    "En el Grado en Ingeniería Biomédica, los estudiantes pueden realizar hasta "
                    "1.800 horas de prácticas extracurriculares. No incluye prácticas curriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_grado_biomedica", "role": "estudiante", "school": "ETSII"}
            ),
            Document(
                page_content=(
                    "En el Doble Grado en Ciencia de Datos y Organización Industrial, los estudiantes pueden realizar hasta "
                    "2.801,25 horas de prácticas extracurriculares. No incluye prácticas curriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_doble_grado_datos_org_industrial", "role": "estudiante", "school": "ETSII"}
            ),

            # ------------------ MÁSTERES ADICIONALES ------------------
            Document(
                page_content=(
                    "En el Máster Universitario en Ingeniería Industrial, los estudiantes pueden realizar hasta "
                    "1.200 horas de prácticas extracurriculares y 225 horas de prácticas curriculares (9 ECTS)."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_ingenieria_industrial", "role": "estudiante", "school": "ETSII"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Ingeniería Química, los estudiantes pueden realizar hasta "
                    "1.200 horas de prácticas extracurriculares y 225 horas de prácticas curriculares (9 ECTS)."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_ingenieria_quimica", "role": "estudiante", "school": "ETSII"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Ingeniería Biomédica, los estudiantes pueden realizar hasta "
                    "900 horas de prácticas extracurriculares, 300 horas de prácticas curriculares obligatorias (12 ECTS) "
                    "y 450 horas de prácticas curriculares optativas para itinerarios GIB (18 ECTS)."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_biomedica", "role": "estudiante", "school": "ETSII"}
            ),
        ]

        print("📄 Chunks manuales de ETSII actualizados correctamente.")
        return manual_etsii

    except Exception as e:
        print(f"⚠️ ETSII no cargada: {e}")
        return []
