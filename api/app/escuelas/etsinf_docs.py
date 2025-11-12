from langchain.schema import Document
from app.loader import cargar_documentos_y_tabla
from pathlib import Path
import os

def cargar_docs_etsinf():
    
    try:
        DATA_DIR = Path(os.getenv("DATA_DIR", Path(__file__).resolve().parents[1] / "Datos")).resolve()
        RUTA_TABLA_ETSINF = str(DATA_DIR / "Informacion-Practicas-Externas-ETSINF.pdf")

        overlay_etsinf = cargar_documentos_y_tabla(
            archivos_pdf=[],
            ruta_tabla_pdf=RUTA_TABLA_ETSINF,
            role="estudiante",
            school="ETSINF",
            solo_tabla=True,
        )

        print("ETSINF cargado")
        return overlay_etsinf

    except Exception as e:
        print(f"⚠️ ETSINF no cargada: {e}")
        return []
