from langchain.schema import Document
from pathlib import Path
import os

from langchain.schema import Document

def cargar_docs_epsa():
    """Carga los documentos manuales actualizados de la EPSA (Escuela Politécnica Superior de Alcoy-UPV)."""
    try:
        manual_epsa = [
            # --- Definición general y obligatoriedad ---
            Document(
                page_content=(
                    "En la Escuela Politécnica Superior de Alcoy (EPSA-UPV), las prácticas curriculares son de carácter voluntario, "
                    "excepto en el Doble Grado en Administración y Dirección de Empresas (ADE) y Gestión Turística, donde son obligatorias "
                    "y corresponden a 18 créditos ECTS vinculados al área de Turismo."
                ),
                metadata={"source": "manual", "categoria": "obligatoriedad_practicas", "role": "estudiante", "school": "EPSA"}
            ),

            # ------------------ GRADOS ------------------
            Document(
                page_content=(
                    "En el Grado en Diseño Industrial y Desarrollo del Producto (EPSA-UPV), las prácticas curriculares tienen una carga de "
                    "18 ECTS (450 horas) y los estudiantes pueden realizar hasta 1.800 horas de prácticas extracurriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_grado_diseno_industrial", "role": "estudiante", "school": "EPSA"}
            ),
            Document(
                page_content=(
                    "En el Grado en Administración y Dirección de Empresas (EPSA-UPV), las prácticas curriculares tienen una carga de "
                    "13,5 ECTS (337,5 horas) y los estudiantes pueden realizar hasta 1.800 horas de prácticas extracurriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_grado_ade", "role": "estudiante", "school": "EPSA"}
            ),
            Document(
                page_content=(
                    "En el Grado en Ingeniería Informática (EPSA-UPV), las prácticas curriculares tienen una carga de "
                    "18 ECTS (450 horas) y se pueden realizar hasta 1.800 horas de prácticas extracurriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_grado_informatica", "role": "estudiante", "school": "EPSA"}
            ),
            Document(
                page_content=(
                    "En el Grado en Ingeniería Eléctrica (EPSA-UPV), las prácticas curriculares tienen una carga de "
                    "18 ECTS (450 horas) y se pueden realizar hasta 1.800 horas de prácticas extracurriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_grado_electrica", "role": "estudiante", "school": "EPSA"}
            ),
            Document(
                page_content=(
                    "En el Grado en Ingeniería Química (plan nuevo 188, EPSA-UPV), las prácticas curriculares tienen una carga de "
                    "4,5 ECTS (112,5 horas) y se pueden realizar hasta 1.800 horas de prácticas extracurriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_grado_quimica_188", "role": "estudiante", "school": "EPSA"}
            ),
            Document(
                page_content=(
                    "En el Grado en Ingeniería Mecánica (EPSA-UPV), las prácticas curriculares tienen una carga de "
                    "18 ECTS (450 horas) y se pueden realizar hasta 1.800 horas de prácticas extracurriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_grado_mecanica", "role": "estudiante", "school": "EPSA"}
            ),
            Document(
                page_content=(
                    "En el Grado en Informática Industrial y Robótica (EPSA-UPV), las prácticas curriculares tienen una carga de "
                    "18 ECTS (450 horas) y se pueden realizar hasta 1.800 horas de prácticas extracurriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_grado_informatica_industrial_robotica", "role": "estudiante", "school": "EPSA"}
            ),

            # ------------------ DOBLES GRADOS ------------------
            Document(
                page_content=(
                    "En el Doble Grado en Administración y Dirección de Empresas y Gestión Turística (EPSA-UPV), "
                    "las prácticas curriculares son obligatorias y tienen una carga de 18 ECTS (450 horas), "
                    "relacionadas con el ámbito del turismo. El número máximo de horas de prácticas extracurriculares es de 2.700."
                ),
                metadata={"source": "manual", "categoria": "practicas_doble_grado_ade_turismo", "role": "estudiante", "school": "EPSA"}
            ),
            Document(
                page_content=(
                    "En el Doble Grado en Administración y Dirección de Empresas e Informática (EPSA-UPV), "
                    "solo se contemplan prácticas extracurriculares, con un máximo de 2.700 horas."
                ),
                metadata={"source": "manual", "categoria": "practicas_doble_grado_ade_informatica", "role": "estudiante", "school": "EPSA"}
            ),

            # ------------------ MÁSTERES ------------------
            Document(
                page_content=(
                    "En el Máster Universitario en Ingeniería Textil (plan nuevo, código 2294, 90 ECTS, EPSA-UPV), "
                    "las prácticas curriculares tienen una carga de 9 ECTS (225 horas) y pueden realizarse hasta 900 horas de prácticas extracurriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_ingenieria_textil", "role": "estudiante", "school": "EPSA"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Ingeniería de Organización y Logística (EPSA-UPV), "
                    "las prácticas curriculares tienen una carga de 6 ECTS (150 horas) y pueden realizarse hasta 900 horas de prácticas extracurriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_organizacion_logistica", "role": "estudiante", "school": "EPSA"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Ingeniería, Procesamiento y Caracterización de Materiales (EPSA-UPV), "
                    "las prácticas curriculares tienen una carga de 9 ECTS (225 horas) y pueden realizarse hasta 900 horas de prácticas extracurriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_materiales", "role": "estudiante", "school": "EPSA"}
            ),
            Document(
                page_content=(
                    "En el Máster Universitario en Dirección de Empresas (MBA, EPSA-UPV), "
                    "las prácticas curriculares tienen una carga de 9 ECTS (225 horas) y pueden realizarse hasta 900 horas de prácticas extracurriculares."
                ),
                metadata={"source": "manual", "categoria": "practicas_master_mba", "role": "estudiante", "school": "EPSA"}
            ),
        ]

        print("📄 Chunks manuales de EPSA actualizados correctamente.")
        return manual_epsa

    except Exception as e:
        print(f"⚠️ EPSA no cargada: {e}")
        return []
