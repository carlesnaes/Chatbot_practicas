from langchain.schema import Document

def cargar_docs_umu():
    """Carga los documentos manuales actualizados de los Másteres Universitarios (UMU-UPV)."""
    try:
        manual_umu = [
            # ------------------ MÁSTERES (primera tabla) ------------------
            Document(
                page_content=(
                    "En el Máster Universitario en Acuicultura (UMU-UPV), las prácticas curriculares son de 6 ECTS (150 horas) "
                    "y pueden realizarse hasta 600 horas de prácticas extracurriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_acuicultura", "role": "estudiante", "school": "UMU"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Computación en la Nube y de Altas Prestaciones (UMU-UPV), "
                    "no se incluyen prácticas curriculares. El máximo de prácticas extracurriculares es de 600 horas."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_cloud_hpc", "role": "estudiante", "school": "UMU"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Cooperación al Desarrollo (UMU-UPV), "
                    "las prácticas curriculares son de 20 ECTS (500 horas) y pueden realizarse hasta 900 horas de prácticas extracurriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_cooperacion_desarrollo", "role": "estudiante", "school": "UMU"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Gestión Cultural (UMU-UPV), "
                    "las prácticas curriculares son de 5 ECTS (125 horas) y pueden realizarse hasta 750 horas de prácticas extracurriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_gestion_cultural", "role": "estudiante", "school": "UMU"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Gestión de la Seguridad y Calidad Alimentaria (UMU-UPV), "
                    "las prácticas curriculares son de 8 ECTS (200 horas) y pueden realizarse hasta 600 horas de prácticas extracurriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_seguridad_calidad_alimentaria", "role": "estudiante", "school": "UMU"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Análisis de Datos, Mejora de Procesos y Toma de Decisiones (UMU-UPV), "
                    "las prácticas curriculares son de 8 ECTS (200 horas) y pueden realizarse hasta 600 horas de prácticas extracurriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_analisis_datos", "role": "estudiante", "school": "UMU"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Ingeniería y Tecnología de Sistemas Software (UMU-UPV), "
                    "las prácticas curriculares son de 6 ECTS (150 horas) y pueden realizarse hasta 600 horas de prácticas extracurriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_sistemas_software", "role": "estudiante", "school": "UMU"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Inteligencia Artificial, Reconocimiento de Formas e Imagen Digital (UMU-UPV), "
                    "no se incluyen prácticas curriculares. El máximo de horas extracurriculares es de 600."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_inteligencia_artificial", "role": "estudiante", "school": "UMU"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Investigación Matemática (UMU-UPV), "
                    "no se incluyen prácticas curriculares. El máximo de horas extracurriculares es de 600."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_investigacion_matematica", "role": "estudiante", "school": "UMU"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Lenguas y Tecnología (UMU-UPV), "
                    "no se contemplan prácticas curriculares. El máximo de horas extracurriculares es de 600."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_lenguas_tecnologia", "role": "estudiante", "school": "UMU"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Mejora Genética Animal y Biotecnología de la Reproducción (UMU-UPV), "
                    "no se incluyen prácticas curriculares. El máximo de horas extracurriculares es de 1.200."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_mejora_genetica_animal", "role": "estudiante", "school": "UMU"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Mejora Genética Vegetal (UMU-UPV), "
                    "no se incluyen prácticas curriculares. El máximo de horas extracurriculares es de 1.200."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_mejora_genetica_vegetal", "role": "estudiante", "school": "UMU"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Sistemas Propulsivos para una Movilidad Sostenible (UMU-UPV), "
                    "las prácticas curriculares son de 18 ECTS (450 horas) y pueden realizarse hasta 1.200 horas de prácticas extracurriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_sistemas_propulsivos", "role": "estudiante", "school": "UMU"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Producción Animal (UMU-UPV), "
                    "no se contemplan prácticas curriculares. El máximo de horas extracurriculares es de 600."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_produccion_animal", "role": "estudiante", "school": "UMU"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Química Sostenible (UMU-UPV), "
                    "no se contemplan prácticas curriculares. El máximo de horas extracurriculares es de 600."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_quimica_sostenible", "role": "estudiante", "school": "UMU"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Enología (UMU-UPV), "
                    "no se incluyen prácticas curriculares. El máximo de horas extracurriculares es de 600."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_enologia", "role": "estudiante", "school": "UMU"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Estudios de la Ciencia, Tecnología e Innovación (UMU-UPV), "
                    "las prácticas curriculares son de 6 ECTS (150 horas) y pueden realizarse hasta 600 horas de prácticas extracurriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_estudios_ciencia", "role": "estudiante", "school": "UMU"}
            ),

            # ------------------ SEGUNDA TABLA ------------------
            Document(
                page_content=(
                    "En el Máster Universitario en Biotecnología Biomédica (UMU-UPV), "
                    "las prácticas curriculares son de 6 ECTS (150 horas) y pueden realizarse hasta 900 horas de prácticas extracurriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_biotecnologia_biomedica", "role": "estudiante", "school": "UMU"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Biotecnología Molecular y Celular de Plantas (UMU-UPV), "
                    "no se incluyen prácticas curriculares. El máximo de horas extracurriculares es de 900."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_biotecnologia_plantas", "role": "estudiante", "school": "UMU"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Economía Agroalimentaria y del Medio Ambiente (UMU-UPV), "
                    "las prácticas curriculares son de 6 ECTS (150 horas) y pueden realizarse hasta 600 horas de prácticas extracurriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_economia_agroalimentaria", "role": "estudiante", "school": "UMU"}
            ),
            Document(
                page_content=(
                    "En el Máster Erasmus Mundus en Sanidad Vegetal en Agricultura Sostenible (UMU-UPV), "
                    "no se incluyen prácticas curriculares. El máximo de horas extracurriculares es de 1.200."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_erasmus_sanidad_vegetal", "role": "estudiante", "school": "UMU"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Ingeniería del Hormigón (UMU-UPV), "
                    "las prácticas curriculares son de 5 ECTS (125 horas) y pueden realizarse hasta 900 horas de prácticas extracurriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_ingenieria_hormigon", "role": "estudiante", "school": "UMU"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Ciencias e Ingeniería de los Alimentos (UMU-UPV), "
                    "las prácticas curriculares son de 8 ECTS (200 horas) y pueden realizarse hasta 600 horas de prácticas extracurriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_ciencias_alimentos", "role": "estudiante", "school": "UMU"}
            ),
        ]

        print("📄 Chunks manuales de UMU actualizados correctamente.")
        return manual_umu

    except Exception as e:
        print(f"⚠️ UMU no cargada: {e}")
        return []
