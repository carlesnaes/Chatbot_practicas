from langchain.schema import Document

def cargar_docs_etsiadi():
    """Carga los documentos manuales actualizados de la ETSIADI (Ingeniería Aeroespacial y Diseño Industrial-UPV)."""
    try:
        manual_etsiadi = [
            # ------------------ GRADOS ------------------
            Document(
                page_content=(
                    "En el Grado en Ingeniería Aeroespacial (ETSIADI-UPV), los estudiantes pueden realizar hasta "
                    "1.800 horas de prácticas extracurriculares y 450 horas de prácticas curriculares optativas (18 ECTS)."
                ),
                metadata={"source": "manual", "categoria": "practicas_grado_aeroespacial", "role": "estudiante", "school": "ETSIADI"}
            ),
            Document(
                page_content=(
                    "En el Grado en Ingeniería Eléctrica (ETSIADI-UPV), los estudiantes pueden realizar hasta "
                    "1.800 horas de prácticas extracurriculares y 450 horas de prácticas curriculares optativas (18 ECTS)."
                ),
                metadata={"source": "manual", "categoria": "practicas_grado_electrica", "role": "estudiante", "school": "ETSIADI"}
            ),
            Document(
                page_content=(
                    "En el Grado en Ingeniería Electrónica Industrial y Automática (ETSIADI-UPV), los estudiantes pueden realizar hasta "
                    "1.800 horas de prácticas extracurriculares y 450 horas de prácticas curriculares optativas (18 ECTS)."
                ),
                metadata={"source": "manual", "categoria": "practicas_grado_electronica_industrial", "role": "estudiante", "school": "ETSIADI"}
            ),
            Document(
                page_content=(
                    "En el Grado en Ingeniería en Diseño Industrial y Desarrollo de Productos (ETSIADI-UPV), los estudiantes pueden realizar hasta "
                    "1.800 horas de prácticas extracurriculares y 450 horas de prácticas curriculares optativas (18 ECTS)."
                ),
                metadata={"source": "manual", "categoria": "practicas_grado_diseno_industrial", "role": "estudiante", "school": "ETSIADI"}
            ),
            Document(
                page_content=(
                    "En el Grado en Ingeniería Mecánica (ETSIADI-UPV), los estudiantes pueden realizar hasta "
                    "1.800 horas de prácticas extracurriculares y 450 horas de prácticas curriculares optativas (18 ECTS)."
                ),
                metadata={"source": "manual", "categoria": "practicas_grado_mecanica", "role": "estudiante", "school": "ETSIADI"}
            ),

            # ------------------ MÁSTERES ------------------
            Document(
                page_content=(
                    "En el Máster Universitario en Diseño y Fabricación Integrada (CAD-CAM-CIM) (ETSIADI-UPV), "
                    "los estudiantes pueden realizar hasta 600 horas de prácticas extracurriculares y 200 horas de prácticas curriculares obligatorias (8 ECTS)."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_cad_cam_cim", "role": "estudiante", "school": "ETSIADI"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Ingeniería del Diseño (nuevo plan, ETSIADI-UPV), "
                    "los estudiantes pueden realizar hasta 900 horas de prácticas extracurriculares y 375 horas de prácticas curriculares optativas (15 ECTS)."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_diseno_nuevo_plan", "role": "estudiante", "school": "ETSIADI"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Ingeniería del Diseño (plan a extinguir, ETSIADI-UPV), "
                    "los estudiantes pueden realizar hasta 750 horas de prácticas extracurriculares. Este plan no incluye prácticas curriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_diseno_antiguo", "role": "estudiante", "school": "ETSIADI"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Ingeniería Mecatrónica (ETSIADI-UPV), los estudiantes pueden realizar hasta "
                    "900 horas de prácticas extracurriculares. Este máster no incluye prácticas curriculares en su plan de estudios."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_mecatronica", "role": "estudiante", "school": "ETSIADI"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Ingeniería Aeronáutica (ETSIADI-UPV), los estudiantes pueden realizar hasta "
                    "1.200 horas de prácticas extracurriculares y 337,5 horas de prácticas curriculares optativas (13,5 ECTS)."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_aeronautica", "role": "estudiante", "school": "ETSIADI"}
            ),
            Document(
                page_content=(
                    "En el Máster en Ingeniería del Mantenimiento (nuevo plan, ETSIADI-UPV), los estudiantes pueden realizar hasta "
                    "900 horas de prácticas extracurriculares y 300 horas de prácticas curriculares obligatorias (12 ECTS)."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_mantenimiento_nuevo", "role": "estudiante", "school": "ETSIADI"}
            ),
            Document(
                page_content=(
                    "En el Máster en Ingeniería del Mantenimiento (plan a extinguir, ETSIADI-UPV), los estudiantes pueden realizar hasta "
                    "720 horas de prácticas extracurriculares y 150 horas de prácticas curriculares obligatorias (6 ECTS)."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_mantenimiento_antiguo", "role": "estudiante", "school": "ETSIADI"}
            ),
            Document(
                page_content=(
                    "En el Máster en Mecánica de Fluidos Computacional (ETSIADI-UPV), los estudiantes pueden realizar hasta "
                    "900 horas de prácticas extracurriculares y 337,5 horas de prácticas curriculares optativas (13,5 ECTS)."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_fluidos", "role": "estudiante", "school": "ETSIADI"}
            ),
            Document(
                page_content=(
                    "En el Máster en Ingeniería en Movilidad Eléctrica (ETSIADI-UPV), los estudiantes pueden realizar hasta "
                    "900 horas de prácticas extracurriculares y 337,5 horas de prácticas curriculares optativas (13,5 ECTS)."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_movilidad_electrica", "role": "estudiante", "school": "ETSIADI"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Sistemas de Aeronaves no Tripuladas y Tecnologías Asociadas (ETSIADI-UPV), "
                    "los estudiantes pueden realizar hasta 900 horas de prácticas extracurriculares y 450 horas de prácticas curriculares optativas (15 ECTS)."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_drones_sistemas_aeronaves", "role": "estudiante", "school": "ETSIADI"}
            ),
        ]

        print("📄 Chunks manuales de ETSIADI actualizados correctamente.")
        return manual_etsiadi

    except Exception as e:
        print(f"⚠️ ETSIADI no cargada: {e}")
        return []
