from langchain.schema import Document

def cargar_docs_etsigct():
    """Carga los documentos manuales de la ETSIGCT (Ingeniería Geodésica, Cartográfica y Topográfica-UPV)."""
    try:
        manual_etsigct = [
            # --- Prácticas curriculares ---
            Document(
                page_content=(
                    "En la ETSIGCT (Escuela Técnica Superior de Ingeniería Geodésica, Cartográfica y Topográfica-UPV), "
                    "las prácticas curriculares tienen una duración mínima de 0,5 créditos ECTS (12,5 horas) "
                    "y una duración máxima de 6 créditos ECTS (150 horas). "
                    "Son de carácter optativo y se aplican tanto a titulaciones de grado como de máster."
                ),
                metadata={
                    "source": "manual",
                    "categoria": "practicas_curriculares_limites",
                    "role": "estudiante",
                    "school": "ETSIGCT"
                }
            ),

            # --- Prácticas extracurriculares ---
            Document(
                page_content=(
                    "En la ETSIGCT (Escuela Técnica Superior de Ingeniería Geodésica, Cartográfica y Topográfica-UPV), "
                    "las prácticas extracurriculares tienen una duración mínima de 0,5 créditos ECTS (12,5 horas). "
                    "La duración máxima es de 1.800 horas para los grados y de 1.200 horas para los másteres."
                ),
                metadata={
                    "source": "manual",
                    "categoria": "practicas_extracurriculares_limites",
                    "role": "estudiante",
                    "school": "ETSIGCT"
                }
            )
        ]

        print("📄 Chunks manuales de ETSIGCT actualizados correctamente.")
        return manual_etsigct

    except Exception as e:
        print(f"⚠️ ETSIGCT no cargada: {e}")
        return []
