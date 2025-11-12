from langchain.schema import Document

def cargar_docs_etsit():
    """Carga los documentos manuales actualizados de la ETSIT (Escuela Técnica Superior de Ingenieros de Telecomunicación-UPV)."""
    try:
        manual_etsit = [
            # --- Condiciones generales ---
            Document(
                page_content=(
                    "Los estudiantes de Grado deben haber superado todo el primer curso y al menos el 50% de los créditos totales "
                    "para poder realizar prácticas curriculares o extracurriculares. "
                    "Además, deben estar matriculados en los créditos correspondientes a las prácticas."
                ),
                metadata={"source": "manual", "categoria": "condiciones_generales_practicas", "role": "estudiante", "school": "ETSIT"}
            ),

            # --- Prácticas curriculares ---
            Document(
                page_content=(
                    "Las prácticas curriculares en la ETSIT pueden realizarse a partir del segundo curso, "
                    "siempre que se haya superado completamente el primer curso y al menos el 50% de los créditos totales del grado. "
                    "El estudiante debe estar matriculado en los créditos de prácticas curriculares antes de su inicio."
                ),
                metadata={"source": "manual", "categoria": "practicas_curriculares_condiciones", "role": "estudiante", "school": "ETSIT"}
            ),

            # --- Prácticas extracurriculares ---
            Document(
                page_content=(
                    "Para realizar prácticas extracurriculares en la ETSIT, los estudiantes de Grado deben haber superado al menos "
                    "el 50% de los créditos totales. Los estudiantes de Máster deben presentar la propuesta de práctica con una "
                    "antelación mínima de 20 días respecto a la fecha de inicio prevista, a través de la plataforma Policonsulta "
                    "o en la Oficina de Relaciones Internacionales y Prácticas en Empresa, para su valoración y autorización."
                ),
                metadata={"source": "manual", "categoria": "practicas_extracurriculares_condiciones", "role": "estudiante", "school": "ETSIT"}
            ),

            # --- Máster Universitario en Ingeniería de Telecomunicación (MUIT) ---
            Document(
                page_content=(
                    "Las prácticas del Máster Universitario en Ingeniería de Telecomunicación (MUIT) se realizan durante el segundo curso, "
                    "aunque excepcionalmente pueden realizarse durante el primero con autorización expresa. "
                    "Estas prácticas se desarrollan exclusivamente en Institutos de la UPV, pudiendo ser curriculares o extracurriculares, "
                    "y deben incluir el compromiso de realizar el Trabajo Fin de Máster (TFM). "
                    "La duración mínima es de seis meses, y la retribución mínima establecida es de 7 euros brutos por hora.\n\n"
                    "Jornadas permitidas:\n"
                    "• Cuatrimestre A: 20–25 horas/semana.\n"
                    "• Cuatrimestre B: 20–40 horas/semana.\n\n"
                    "Las prácticas requieren autorización del Subdirector de Cátedras, Emprendimiento y Empleo."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_telecomunicacion", "role": "estudiante", "school": "ETSIT"}
            ),

            # --- Limitaciones horarias ---
            Document(
                page_content=(
                    "Para estudiantes matriculados a tiempo completo (60 ECTS o más), se aplican las siguientes limitaciones horarias:\n\n"
                    "• Durante el período lectivo: máximo 16 horas semanales si la práctica se realiza en una empresa externa a la UPV, "
                    "y máximo 20 horas semanales si la práctica se realiza dentro de la UPV.\n"
                    "• Durante el período no lectivo: máximo 40 horas semanales.\n\n"
                    "Estas limitaciones no se aplican a estudiantes con matrícula parcial."
                ),
                metadata={"source": "manual", "categoria": "limitaciones_horarias_practicas", "role": "estudiante", "school": "ETSIT"}
            ),
        ]

        print("📄 Chunks manuales de ETSIT actualizados correctamente.")
        return manual_etsit

    except Exception as e:
        print(f"⚠️ ETSIT no cargada: {e}")
        return []
