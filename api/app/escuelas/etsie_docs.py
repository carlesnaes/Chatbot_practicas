from langchain.schema import Document

def cargar_docs_etsie():
    """Carga los documentos manuales actualizados de la ETSIE (Escuela Técnica Superior de Ingeniería de Edificación-UPV)."""
    try:
        manual_etsie = [
            # --- Grado en Arquitectura Técnica ---
            Document(
                page_content=(
                    "En la ETSIE (Escuela Técnica Superior de Ingeniería de Edificación-UPV), "
                    "las prácticas curriculares del Grado en Arquitectura Técnica se estructuran en:\n\n"
                    "• Obligatoria – 6 ECTS (150 horas)\n"
                    "• Optativa de Intensificación – 12 ECTS (300 horas)\n\n"
                    "Las prácticas optativas de intensificación solo pueden realizarse si van asociadas al TFG en la modalidad de convenio con empresa. "
                    "Ambas pueden reconocerse conjuntamente (18 ECTS / 450 horas) junto con el TFG. "
                    "Además, los estudiantes pueden realizar hasta 1.800 horas de prácticas extracurriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_grado_arquitectura_tecnica", "role": "estudiante", "school": "ETSIE"}
            ),

            # --- Máster Universitario en Edificación ---
            Document(
                page_content=(
                    "En el Máster Universitario en Edificación (ETSIE-UPV), "
                    "las prácticas curriculares son optativas (materia Praktikum) y pueden alcanzar hasta 18 ECTS (450 horas), "
                    "realizándose en el primer semestre del segundo curso. "
                    "Los estudiantes pueden realizar además hasta 900 horas de prácticas extracurriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_edificacion", "role": "estudiante", "school": "ETSIE"}
            ),

            # --- Máster Universitario en Rehabilitación y Sostenibilidad en Edificios ---
            Document(
                page_content=(
                    "En el Máster Universitario en Rehabilitación y Sostenibilidad en Edificios (ETSIE-UPV), "
                    "las prácticas curriculares son obligatorias con una carga de 3 ECTS (75 horas), realizables durante todo el curso. "
                    "Los estudiantes pueden realizar además hasta 600 horas de prácticas extracurriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_rehabilitacion", "role": "estudiante", "school": "ETSIE"}
            ),

            # --- Recomendaciones: Matrícula y normativa general ---
            Document(
                page_content=(
                    "La matrícula de créditos curriculares se realiza en cualquier momento tras tener empresa, "
                    "mediante PoliConsulta a la Secretaría del Centro junto con el documento de convenio."
                ),
                metadata={"source": "manual", "categoria": "recomendacion_matricula_practicas", "role": "estudiante", "school": "ETSIE"}
            ),
            Document(
                page_content=(
                    "Matricular los créditos no garantiza la realización de las prácticas; "
                    "se deben cumplir los requisitos establecidos en la normativa de la UPV y del plan de estudios."
                ),
                metadata={"source": "manual", "categoria": "recomendacion_normativa_upv", "role": "estudiante", "school": "ETSIE"}
            ),
            Document(
                page_content=(
                    "Las prácticas se realizan entre el 1 de septiembre y el 31 de agosto, sin interferir con la docencia. "
                    "No se conceden dispensas de asistencia a clase."
                ),
                metadata={"source": "manual", "categoria": "recomendacion_periodo_realizacion", "role": "estudiante", "school": "ETSIE"}
            ),

            # --- Recomendaciones específicas del Grado en Arquitectura Técnica ---
            Document(
                page_content=(
                    "Las prácticas optativas (12 ECTS) y el TFG (12 ECTS) deben realizarse simultáneamente dentro del mismo itinerario curricular, "
                    "siendo el TFG en modalidad de convenio con empresa."
                ),
                metadata={"source": "manual", "categoria": "recomendacion_itinerario_tfg", "role": "estudiante", "school": "ETSIE"}
            ),
            Document(
                page_content=(
                    "No se deben matricular los 12 ECTS optativos hasta haber acordado la realización de las prácticas vinculadas a esos créditos y al TFG."
                ),
                metadata={"source": "manual", "categoria": "recomendacion_matricula_optativas", "role": "estudiante", "school": "ETSIE"}
            ),
            Document(
                page_content=(
                    "Si no se han cursado previamente las prácticas obligatorias (6 ECTS), "
                    "pueden agruparse en el último cuatrimestre junto a las optativas (12 ECTS) y el TFG (12 ECTS)."
                ),
                metadata={"source": "manual", "categoria": "recomendacion_agrupacion_final", "role": "estudiante", "school": "ETSIE"}
            ),
            Document(
                page_content=(
                    "Si las prácticas obligatorias (6 ECTS) se realizan al final y no se sigue el itinerario de intensificación, "
                    "deben vincularse a la línea temática del área de intensificación elegida y al TFG."
                ),
                metadata={"source": "manual", "categoria": "recomendacion_vinculacion_tematica", "role": "estudiante", "school": "ETSIE"}
            ),

            # --- Recomendaciones específicas de máster ---
            Document(
                page_content=(
                    "No se deben matricular los 18 ECTS curriculares optativos del Máster en Edificación "
                    "hasta haber encontrado empresa para la realización de las prácticas."
                ),
                metadata={"source": "manual", "categoria": "recomendacion_matricula_master_edificacion", "role": "estudiante", "school": "ETSIE"}
            ),
        ]

        print("📄 Chunks manuales de ETSIE actualizados correctamente.")
        return manual_etsie

    except Exception as e:
        print(f"⚠️ ETSIE no cargada: {e}")
        return []
