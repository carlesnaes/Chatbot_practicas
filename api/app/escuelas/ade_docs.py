from langchain.schema import Document

def cargar_docs_ade():
    """Carga los documentos manuales de la Facultad de Administración y Dirección de Empresas (ADE-UPV)."""
    try:
        manual_ade = [
            # ------------------ GRADOS ------------------
            Document(
                page_content=(
                    "En el Grado en Administración y Dirección de Empresas (ADE-UPV), "
                    "los estudiantes pueden realizar hasta 1.800 horas de prácticas extracurriculares "
                    "y 337,5 horas de prácticas curriculares, equivalentes a 13,5 créditos ECTS."
                ),
                metadata={"source": "manual", "categoria": "practicas_grado_ade", "role": "estudiante", "school": "ADE"}
            ),
            Document(
                page_content=(
                    "En el Grado en Gestión y Administración Pública (ADE-UPV), "
                    "los estudiantes pueden realizar hasta 1.800 horas de prácticas extracurriculares "
                    "y 450 horas de prácticas curriculares, equivalentes a 18 créditos ECTS."
                ),
                metadata={"source": "manual", "categoria": "practicas_grado_gestion_publica", "role": "estudiante", "school": "ADE"}
            ),

            # ------------------ MÁSTERES ------------------
            Document(
                page_content=(
                    "En el Máster Universitario en Gestión de Empresas, Servicios y Productos, "
                    "los estudiantes pueden realizar hasta 900 horas de prácticas extracurriculares "
                    "y 300 horas de prácticas curriculares (12 créditos ECTS)."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_gestion_empresas", "role": "estudiante", "school": "ADE"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Dirección Financiera y Fiscal, "
                    "los estudiantes pueden realizar hasta 600 horas de prácticas extracurriculares. "
                    "Este máster no contempla prácticas curriculares obligatorias."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_financiera_fiscal", "role": "estudiante", "school": "ADE"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Gestión Administrativa, "
                    "los estudiantes pueden realizar hasta 600 horas de prácticas extracurriculares "
                    "y 225 horas de prácticas curriculares obligatorias (9 créditos ECTS)."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_gestion_administrativa", "role": "estudiante", "school": "ADE"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Social Media y Comunicación Corporativa, "
                    "los estudiantes pueden realizar hasta 600 horas de prácticas extracurriculares "
                    "y 300 horas de prácticas curriculares (12 créditos ECTS)."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_social_media", "role": "estudiante", "school": "ADE"}
            ),

            # ------------------ DOBLES GRADOS ------------------
            Document(
                page_content=(
                    "En el Doble Grado en Ingeniería de Tecnologías y Servicios de Telecomunicación y Grado en Administración y Dirección de Empresas, "
                    "los estudiantes pueden realizar hasta 2.778 horas de prácticas extracurriculares. "
                    "No se establecen prácticas curriculares específicas para este doble grado."
                ),
                metadata={"source": "manual", "categoria": "practicas_doble_grado_teleco_ade", "role": "estudiante", "school": "ADE"}
            ),
            Document(
                page_content=(
                    "En el Doble Grado en Administración y Dirección de Empresas y Grado en Ingeniería Informática, "
                    "los estudiantes pueden realizar hasta 2.801 horas de prácticas extracurriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_doble_grado_ade_informatica", "role": "estudiante", "school": "ADE"}
            ),
            Document(
                page_content=(
                    "En el Doble Grado en Administración y Dirección de Empresas y Grado en Ciencia y Tecnología de los Alimentos, "
                    "los estudiantes pueden realizar hasta 2.801 horas de prácticas extracurriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_doble_grado_ade_alimentos", "role": "estudiante", "school": "ADE"}
            ),
            Document(
                page_content=(
                    "En la Doble Titulación de Grado en Administración y Dirección de Empresas y Grado en Matemáticas, "
                    "los estudiantes pueden realizar hasta 2.632 horas de prácticas extracurriculares. " \
                    "No se establecen prácticas curriculares específicas para esta doble titulación."
                ),
                metadata={"source": "manual", "categoria": "practicas_doble_grado_ade_matematicas", "role": "estudiante", "school": "ADE"}
            )
        ]

        print("Chunks manuales de ADE añadidos correctamente.")
        return manual_ade

    except Exception as e:
        print(f"ADE no cargada: {e}")
        return []
