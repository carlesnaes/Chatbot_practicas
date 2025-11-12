from langchain.schema import Document

def cargar_docs_bbaa():
    """Carga los documentos manuales actualizados de la Facultad de Bellas Artes (BBAA-UPV)."""
    try:
        manual_bbaa = [
            # ------------------ GRADOS ------------------
            Document(
                page_content=(
                    "En el Grado en Bellas Artes (BBAA-UPV), los estudiantes pueden realizar hasta "
                    "1.800 horas de prácticas extracurriculares y 75 horas de prácticas curriculares (3 ECTS). "
                    "Los créditos curriculares se asignan a la Materia 6 del plan de estudios."
                ),
                metadata={"source": "manual", "categoria": "practicas_grado_bellas_artes", "role": "estudiante", "school": "BBAA"}
            ),
            Document(
                page_content=(
                    "En el Grado en Conservación y Restauración de Bienes Culturales (plan nuevo, BBAA-UPV), "
                    "los estudiantes pueden realizar hasta 1.800 horas de prácticas extracurriculares "
                    "y 150 horas de prácticas curriculares (6 ECTS). "
                    "Los créditos curriculares se asignan a la Materia 10 del plan de estudios."
                ),
                metadata={"source": "manual", "categoria": "practicas_grado_restauracion", "role": "estudiante", "school": "BBAA"}
            ),
            Document(
                page_content=(
                    "En el Grado en Diseño y Tecnologías Creativas (BBAA-UPV), los estudiantes pueden realizar hasta "
                    "1.800 horas de prácticas extracurriculares y 150 horas de prácticas curriculares (6 ECTS). "
                    "Los créditos curriculares se asignan a la Materia 6 del plan de estudios."
                ),
                metadata={"source": "manual", "categoria": "practicas_grado_diseno_tecnologias_creativas", "role": "estudiante", "school": "BBAA"}
            ),

            # ------------------ MÁSTERES ------------------
            Document(
                page_content=(
                    "En el Máster Universitario en Producción Artística (BBAA-UPV), los estudiantes pueden realizar hasta "
                    "600 horas de prácticas extracurriculares. Este máster no contempla prácticas curriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_produccion_artistica", "role": "estudiante", "school": "BBAA"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Artes Visuales y Multimedia (BBAA-UPV), los estudiantes pueden realizar hasta "
                    "900 horas de prácticas extracurriculares y 125 horas de prácticas curriculares (5 ECTS). "
                    "Los créditos curriculares se asignan a la materia 'Práctica profesional' del plan de estudios."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_artes_visuales", "role": "estudiante", "school": "BBAA"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Conservación y Restauración de Bienes Culturales (BBAA-UPV), "
                    "los estudiantes pueden realizar hasta 900 horas de prácticas extracurriculares. "
                    "No incluye prácticas curriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_restauracion_bienes_culturales", "role": "estudiante", "school": "BBAA"}
            ),

            # ------------------ RECOMENDACIONES ------------------
            Document(
                page_content=(
                    "La matrícula de créditos curriculares en grado se realiza en cualquier momento tras tener empresa, "
                    "mediante PoliConsulta a la secretaría del centro."
                ),
                metadata={"source": "manual", "categoria": "recomendacion_matricula_practicas", "role": "estudiante", "school": "BBAA"}
            ),
            Document(
                page_content=(
                    "Matricular los créditos no garantiza la realización de las prácticas; se deben cumplir los requisitos "
                    "establecidos por la normativa de la UPV y del plan de estudios."
                ),
                metadata={"source": "manual", "categoria": "recomendacion_normativa", "role": "estudiante", "school": "BBAA"}
            ),
            Document(
                page_content=(
                    "Las prácticas se realizan entre el 1 de septiembre y el 31 de agosto, sin interferir con la docencia. "
                    "No se conceden dispensas de asistencia a clase."
                ),
                metadata={"source": "manual", "categoria": "recomendacion_periodo_realizacion", "role": "estudiante", "school": "BBAA"}
            ),
            Document(
                page_content=(
                    "Para buscar prácticas, el estudiante puede consultar la siguiente página de la Facultad de Bellas Artes: "
                    "https://www.upv.es/contenidos/upebbaa/consejos-para-buscar-practicas/"
                ),
                metadata={"source": "manual", "categoria": "recomendacion_buscar_practicas", "role": "estudiante", "school": "BBAA"}
            ),
            Document(
                page_content=(
                    "Antes de iniciar las prácticas, se recomienda leer los consejos sobre habilidades en el entorno laboral "
                    "disponibles en: https://www.upv.es/contenidos/upebbaa/consejos-antes-de-iniciar-mis-practicas/"
                ),
                metadata={"source": "manual", "categoria": "recomendacion_habilidades_laborales", "role": "estudiante", "school": "BBAA"}
            ),
        ]

        print("📄 Chunks manuales de BBAA actualizados correctamente.")
        return manual_bbaa

    except Exception as e:
        print(f"⚠️ BBAA no cargada: {e}")
        return []
