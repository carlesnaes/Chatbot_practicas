from langchain.schema import Document

def cargar_docs_epsg():
    """Carga los documentos manuales de la Escuela Politécnica Superior de Gandía (EPSG-UPV)."""
    try:
        manual_epsg = [
            # --- Obligatoriedad de prácticas ---
            Document(
                page_content=(
                    "Las prácticas curriculares son de carácter voluntario excepto en el Grado en Turismo, "
                    "en el Doble Grado en Turismo y Administración y Dirección de Empresas (ADE), "
                    "y en el Máster Universitario en Profesor/a de Educación Secundaria."
                ),
                metadata={
                    "source": "manual",
                    "categoria": "obligatoriedad_practicas",
                    "role": "estudiante",
                    "school": "EPSG"
                }
            ),

            # --- GRADOS ---
            Document(
                page_content=(
                    "En el Grado en Ciencias Ambientales (EPSG-UPV), los estudiantes pueden realizar hasta "
                    "1.800 horas de prácticas extracurriculares y 450 horas de prácticas curriculares optativas "
                    "(convalidables como asignaturas optativas, 18 ECTS)."
                ),
                metadata={
                    "source": "manual",
                    "categoria": "practicas_grado_ciencias_ambientales",
                    "role": "estudiante",
                    "school": "EPSG"
                }
            ),
            Document(
                page_content=(
                    "En el Grado en Comunicación Audiovisual (EPSG-UPV), los estudiantes pueden realizar hasta "
                    "1.800 horas de prácticas extracurriculares y 225 horas de prácticas curriculares optativas "
                    "(convalidables como asignaturas optativas, 9 ECTS)."
                ),
                metadata={
                    "source": "manual",
                    "categoria": "practicas_grado_comunicacion_audiovisual",
                    "role": "estudiante",
                    "school": "EPSG"
                }
            ),
            Document(
                page_content=(
                    "En el Grado en Ingeniería de Sistemas de Telecomunicación, Sonido e Imagen (EPSG-UPV), "
                    "los estudiantes pueden realizar hasta 1.800 horas de prácticas extracurriculares "
                    "y 450 horas de prácticas curriculares optativas (convalidables como asignaturas optativas, 18 ECTS)."
                ),
                metadata={
                    "source": "manual",
                    "categoria": "practicas_grado_telecomunicacion_sonido_imagen",
                    "role": "estudiante",
                    "school": "EPSG"
                }
            ),
            Document(
                page_content=(
                    "En el Grado en Tecnologías Interactivas (EPSG-UPV), los estudiantes pueden realizar hasta "
                    "1.800 horas de prácticas extracurriculares y 450 horas de prácticas curriculares optativas "
                    "(convalidables como asignaturas optativas, 18 ECTS)."
                ),
                metadata={
                    "source": "manual",
                    "categoria": "practicas_grado_tecnologias_interactivas",
                    "role": "estudiante",
                    "school": "EPSG"
                }
            ),
            Document(
                page_content=(
                    "En el Grado en Turismo (EPSG-UPV), los estudiantes pueden realizar hasta 1.800 horas de prácticas extracurriculares "
                    "y 450 horas de prácticas curriculares obligatorias (18 ECTS)."
                ),
                metadata={
                    "source": "manual",
                    "categoria": "practicas_grado_turismo",
                    "role": "estudiante",
                    "school": "EPSG"
                }
            ),

            # --- DOBLES GRADOS ---
            Document(
                page_content=(
                    "En el Doble Grado en Administración y Dirección de Empresas (ADE) y Turismo (EPSG-UPV), "
                    "los estudiantes pueden realizar hasta 2.700 horas de prácticas extracurriculares "
                    "y 450 horas de prácticas curriculares obligatorias (18 ECTS)."
                ),
                metadata={
                    "source": "manual",
                    "categoria": "practicas_doble_grado_ade_turismo",
                    "role": "estudiante",
                    "school": "EPSG"
                }
            ),
            Document(
                page_content=(
                    "En el Doble Grado en Ingeniería Forestal y del Medio Natural y Ciencias Ambientales (EPSG-UPV), "
                    "los estudiantes pueden realizar hasta 2.700 horas de prácticas extracurriculares."
                ),
                metadata={
                    "source": "manual",
                    "categoria": "practicas_doble_grado_forestal_ambientales",
                    "role": "estudiante",
                    "school": "EPSG"
                }
            ),
            Document(
                page_content=(
                    "En el Doble Grado en Ingeniería de Sistemas de Telecomunicación, Sonido e Imagen y Comunicación Audiovisual (EPSG-UPV), "
                    "los estudiantes pueden realizar hasta 2.700 horas de prácticas extracurriculares."
                ),
                metadata={
                    "source": "manual",
                    "categoria": "practicas_doble_grado_teleco_audiovisual",
                    "role": "estudiante",
                    "school": "EPSG"
                }
            ),
            Document(
                page_content=(
                    "En el Doble Grado en Ciencias Ambientales y Ciencias y Tecnologías del Mar (EPSG-UPV), "
                    "los estudiantes pueden realizar hasta 2.700 horas de prácticas extracurriculares."
                ),
                metadata={
                    "source": "manual",
                    "categoria": "practicas_doble_grado_ambientales_mar",
                    "role": "estudiante",
                    "school": "EPSG"
                }
            ),

            # --- MÁSTERES ---
            Document(
                page_content=(
                    "En el Máster Universitario en Evaluación y Seguimiento Ambiental de Ecosistemas Marinos y Costeros (EPSG-UPV), "
                    "los estudiantes pueden realizar hasta 600 horas de prácticas extracurriculares y 150 horas de prácticas curriculares optativas "
                    "(convalidables como asignaturas optativas, 6 ECTS)."
                ),
                metadata={
                    "source": "manual",
                    "categoria": "practicas_master_evaluacion_ambiental",
                    "role": "estudiante",
                    "school": "EPSG"
                }
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Comunicación Transmedia (EPSG-UPV), los estudiantes pueden realizar hasta "
                    "600 horas de prácticas extracurriculares."
                ),
                metadata={
                    "source": "manual",
                    "categoria": "practicas_master_comunicacion_transmedia",
                    "role": "estudiante",
                    "school": "EPSG"
                }
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Inteligencia Turística (EPSG-UPV), los estudiantes pueden realizar hasta "
                    "600 horas de prácticas extracurriculares y 150 horas de prácticas curriculares optativas "
                    "(convalidables como asignaturas optativas, 6 ECTS)."
                ),
                metadata={
                    "source": "manual",
                    "categoria": "practicas_master_inteligencia_turistica",
                    "role": "estudiante",
                    "school": "EPSG"
                }
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Postproducción Digital (EPSG-UPV), los estudiantes pueden realizar hasta "
                    "600 horas de prácticas extracurriculares y 100 horas de prácticas curriculares optativas "
                    "(convalidables como asignaturas optativas, 4 ECTS)."
                ),
                metadata={
                    "source": "manual",
                    "categoria": "practicas_master_postproduccion_digital",
                    "role": "estudiante",
                    "school": "EPSG"
                }
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Ingeniería Acústica (EPSG-UPV), los estudiantes pueden realizar hasta "
                    "600 horas de prácticas extracurriculares y 150 horas de prácticas curriculares optativas "
                    "(convalidables como asignaturas optativas, 6 ECTS)."
                ),
                metadata={
                    "source": "manual",
                    "categoria": "practicas_master_ingenieria_acustica",
                    "role": "estudiante",
                    "school": "EPSG"
                }
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Profesor/a de Educación Secundaria (EPSG-UPV), "
                    "los estudiantes pueden realizar hasta 600 horas de prácticas extracurriculares "
                    "y 250 horas de prácticas curriculares obligatorias (10 ECTS)."
                ),
                metadata={
                    "source": "manual",
                    "categoria": "practicas_master_profesorado_secundaria",
                    "role": "estudiante",
                    "school": "EPSG"
                }
            ),
        ]

        print("📄 Chunks manuales de EPSG actualizados correctamente.")
        return manual_epsg

    except Exception as e:
        print(f"⚠️ EPSG no cargada: {e}")
        return []
