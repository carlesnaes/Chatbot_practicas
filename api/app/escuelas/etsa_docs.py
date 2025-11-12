from langchain.schema import Document

def cargar_docs_etsa():
    """Carga los documentos manuales de la Escuela Técnica Superior de Arquitectura (ETSA-UPV)."""
    try:
        manual_etsa = [
            # ------------------ GRADOS ------------------
            Document(
                page_content=(
                    "En el Grado en Fundamentos de la Arquitectura, el número máximo de horas de prácticas "
                    "que un estudiante puede realizar es de 2.250 horas en total."
                ),
                metadata={
                    "source": "manual",
                    "categoria": "practicas_grado_fundamentos_arquitectura",
                    "role": "estudiante",
                    "school": "ETSA"
                }
            ),
            Document(
                page_content=(
                    "En el Grado en Diseño Arquitectónico de Interiores (plan de 4 años), "
                    "los estudiantes pueden realizar hasta 1.800 horas de prácticas extracurriculares "
                    "y 450 horas de prácticas curriculares, equivalentes a 18 créditos ECTS."
                ),
                metadata={
                    "source": "manual",
                    "categoria": "practicas_grado_diseno_interiores",
                    "role": "estudiante",
                    "school": "ETSA"
                }
            ),

            # ------------------ MÁSTERES ------------------
            Document(
                page_content=(
                    "En el Máster Universitario en Arquitectura, los estudiantes pueden realizar hasta 600 horas de prácticas extracurriculares."
                ),
                metadata={
                    "source": "manual",
                    "categoria": "practicas_master_arquitectura",
                    "role": "estudiante",
                    "school": "ETSA"
                }
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Diseño Arquitectónico de Interiores, "
                    "los estudiantes pueden realizar hasta 900 horas de prácticas extracurriculares "
                    "y 450 horas de prácticas curriculares (18 créditos ECTS)."
                ),
                metadata={
                    "source": "manual",
                    "categoria": "practicas_master_diseno_interiores",
                    "role": "estudiante",
                    "school": "ETSA"
                }
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Conservación del Patrimonio Arquitectónico, "
                    "los estudiantes pueden realizar hasta 900 horas de prácticas extracurriculares "
                    "y 337,5 horas de prácticas curriculares (13,5 créditos ECTS)."
                ),
                metadata={
                    "source": "manual",
                    "categoria": "practicas_master_patrimonio",
                    "role": "estudiante",
                    "school": "ETSA"
                }
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Paisaje y Urbanismo, los estudiantes pueden realizar hasta 900 horas de prácticas extracurriculares "
                    "y 337,5 horas de prácticas curriculares (13,5 créditos ECTS)."
                ),
                metadata={
                    "source": "manual",
                    "categoria": "practicas_master_paisaje_urbanismo",
                    "role": "estudiante",
                    "school": "ETSA"
                }
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Innovación en el Hábitat, los estudiantes pueden realizar hasta 900 horas de prácticas extracurriculares "
                    "y 450 horas de prácticas curriculares (18 créditos ECTS)."
                ),
                metadata={
                    "source": "manual",
                    "categoria": "practicas_master_innovacion_habitat",
                    "role": "estudiante",
                    "school": "ETSA"
                }
            ),
        ]

        print("📄 Chunks manuales de ETSA (grados y másteres) añadidos correctamente.")
        return manual_etsa

    except Exception as e:
        print(f"⚠️ ETSA no cargada: {e}")
        return []
