from langchain.schema import Document

def cargar_docs_etsiamn():
    """Carga los documentos manuales actualizados de la ETSIAMN (Ingeniería Agronómica y del Medio Natural-UPV)."""
    try:
        manual_etsiamn = [
            # ------------------ GRADOS ------------------
            Document(
                page_content=(
                    "En el Grado en Biotecnología (ETSIAMN-UPV), los estudiantes deben cursar 6 ECTS curriculares "
                    "(150 horas) en el tercer curso, cuatrimestre B, y pueden realizar hasta 1.800 horas de prácticas extracurriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_grado_biotecnologia", "role": "estudiante", "school": "ETSIAMN"}
            ),
            Document(
                page_content=(
                    "En el Grado en Ciencia y Tecnología de los Alimentos (ETSIAMN-UPV), las prácticas curriculares son de 6 ECTS "
                    "(150 horas), realizadas en el cuarto curso, cuatrimestre A. Además, pueden realizarse hasta 1.800 horas de prácticas extracurriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_grado_ciencia_alimentos", "role": "estudiante", "school": "ETSIAMN"}
            ),
            Document(
                page_content=(
                    "En el Grado en Ingeniería Agroalimentaria y del Medio Rural (ETSIAMN-UPV), los estudiantes cursan 6 ECTS curriculares "
                    "(150 horas) en el segundo curso, cuatrimestre B, y pueden realizar hasta 1.800 horas de prácticas extracurriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_grado_agroalimentaria", "role": "estudiante", "school": "ETSIAMN"}
            ),
            Document(
                page_content=(
                    "En el Grado en Ingeniería Forestal y del Medio Natural (ETSIAMN-UPV), las prácticas curriculares son de 6 ECTS "
                    "(150 horas), realizadas en el cuarto curso, cuatrimestre B, y pueden realizarse hasta 1.800 horas de prácticas extracurriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_grado_forestal", "role": "estudiante", "school": "ETSIAMN"}
            ),

            # ------------------ DOBLES GRADOS ------------------
            Document(
                page_content=(
                    "En el Doble Grado en Biotecnología e Ingeniería Agroalimentaria y del Medio Rural (ETSIAMN-UPV), "
                    "las prácticas curriculares son de 6 ECTS (150 horas) y se realizan en el quinto curso, cuatrimestre B. "
                    "El número máximo de horas de prácticas extracurriculares es de 2.632 horas."
                ),
                metadata={"source": "manual", "categoria": "practicas_doble_grado_biotecnologia_agroalimentaria", "role": "estudiante", "school": "ETSIAMN"}
            ),
            Document(
                page_content=(
                    "En el Doble Grado en Ingeniería Forestal y del Medio Natural y Ciencias Ambientales (ETSIAMN-UPV), "
                    "los estudiantes pueden realizar un máximo de 2.475 horas de prácticas extracurriculares. "
                    "No incluye prácticas curriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_doble_grado_forestal_ambientales", "role": "estudiante", "school": "ETSIAMN"}
            ),
            Document(
                page_content=(
                    "En el Doble Grado en Administración y Dirección de Empresas y Ciencia y Tecnología de los Alimentos (ETSIAMN-UPV), "
                    "los estudiantes pueden realizar hasta 2.947 horas de prácticas extracurriculares. "
                    "No incluye prácticas curriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_doble_grado_ade_alimentos", "role": "estudiante", "school": "ETSIAMN"}
            ),
            Document(
                page_content=(
                    "En el Doble Grado en Ingeniería Agroalimentaria y del Medio Rural y Ciencia y Tecnología de los Alimentos (ETSIAMN-UPV), "
                    "los estudiantes cursan 6 ECTS curriculares (150 horas) en el quinto curso, cuatrimestre A, "
                    "y pueden realizar hasta 2.576 horas de prácticas extracurriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_doble_grado_agroalimentaria_alimentos", "role": "estudiante", "school": "ETSIAMN"}
            ),
            Document(
                page_content=(
                    "En el Doble Grado en Biotecnología y Química (ETSIAMN-UPV), los estudiantes pueden realizar hasta "
                    "2.576 horas de prácticas extracurriculares. No incluye prácticas curriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_doble_grado_biotecnologia_quimica", "role": "estudiante", "school": "ETSIAMN"}
            ),

            # ------------------ MÁSTERES ------------------
            Document(
                page_content=(
                    "En el Máster Universitario en Ingeniería Agronómica (ETSIAMN-UPV), las prácticas curriculares son de 6 ECTS (150 horas) "
                    "y pueden realizarse hasta 1.200 horas de prácticas extracurriculares. "
                    "Durante el segundo curso, el estudiante puede cursar 18 ECTS de asignaturas optativas o combinar hasta tres Prácticum, "
                    "cada uno de 400 horas de prácticas extracurriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_ingenieria_agronomica", "role": "estudiante", "school": "ETSIAMN"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Ingeniería de Montes (ETSIAMN-UPV), las prácticas curriculares son de 6 ECTS (150 horas) "
                    "y pueden realizarse hasta 900 horas de prácticas extracurriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_ingenieria_montes", "role": "estudiante", "school": "ETSIAMN"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Enología (ETSIAMN-UPV), los estudiantes pueden realizar hasta 720 horas de prácticas extracurriculares. "
                    "No incluye prácticas curriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_enologia", "role": "estudiante", "school": "ETSIAMN"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Ganadería de Precisión (ETSIAMN-UPV), las prácticas curriculares son de 12 ECTS "
                    "(300 horas) y pueden realizarse hasta 600 horas de prácticas extracurriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_ganaderia_precision", "role": "estudiante", "school": "ETSIAMN"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Ingeniería Bioambiental y del Paisaje (ETSIAMN-UPV), "
                    "las prácticas curriculares son de 6 ECTS (150 horas) y pueden realizarse hasta 600 horas de prácticas extracurriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_bioambiental_paisaje", "role": "estudiante", "school": "ETSIAMN"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Ciencias de Animales de Laboratorio (ETSIAMN-UPV), "
                    "los estudiantes pueden realizar hasta 600 horas de prácticas extracurriculares. No incluye prácticas curriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_animales_laboratorio", "role": "estudiante", "school": "ETSIAMN"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Sanidad y Producción Vegetal (ETSIAMN-UPV), los estudiantes pueden realizar hasta "
                    "600 horas de prácticas extracurriculares. No incluye prácticas curriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_sanidad_vegetal", "role": "estudiante", "school": "ETSIAMN"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Incendios Forestales, Ciencia y Gestión Integral (ETSIAMN-UPV), "
                    "los estudiantes pueden realizar hasta 900 horas de prácticas extracurriculares. No incluye prácticas curriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_incendios_forestales", "role": "estudiante", "school": "ETSIAMN"}
            ),

            # ------------------ DOBLE MÁSTER ------------------
            Document(
                page_content=(
                    "En los Doble Máster, se deben comprobar las condiciones y la normativa de prácticas de cada uno de los másteres implicados por separado."
                ),
                metadata={"source": "manual", "categoria": "practicas_doble_master", "role": "estudiante", "school": "ETSIAMN"}
            ),

            # ------------------ RECOMENDACIONES ------------------
            Document(
                page_content=(
                    "La matrícula de créditos curriculares se realiza en cualquier momento tras obtener el visto bueno de la "
                    "Unidad de Prácticas en Empresa del centro y presentar el convenio de prácticas correspondiente."
                ),
                metadata={"source": "manual", "categoria": "recomendacion_matricula_practicas", "role": "estudiante", "school": "ETSIAMN"}
            ),
        ]

        print("📄 Chunks manuales de ETSIAMN actualizados correctamente.")
        return manual_etsiamn

    except Exception as e:
        print(f"⚠️ ETSIAMN no cargada: {e}")
        return []
