import os
import requests
from hashlib import md5
from uuid import uuid5, NAMESPACE_URL
from pathlib import Path

from bs4 import BeautifulSoup
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

from typing import Optional, List, Tuple
from loguru import logger

from langchain.schema import Document
from langchain.vectorstores import FAISS




from langchain_openai import OpenAIEmbeddings

from app.escuelas.all_man_chunks import cargar_chunks_manual
from app.loader import cargar_documentos_y_tabla

import inspect

# Escuelas
from app.escuelas.ade_docs import cargar_docs_ade
from app.escuelas.bbaa_docs import cargar_docs_bbaa
from app.escuelas.epsa_docs import cargar_docs_epsa
from app.escuelas.epsg_docs import cargar_docs_epsg
from app.escuelas.etsa_docs import cargar_docs_etsa
from app.escuelas.etsiadi_docs import cargar_docs_etsiadi
from app.escuelas.etsiamn_docs import cargar_docs_etsiamn
from app.escuelas.etsie_docs import cargar_docs_etsie
from app.escuelas.etsii_docs import cargar_docs_etsii
from app.escuelas.etsigct_docs import cargar_docs_etsigct
from app.escuelas.etsinf_docs import cargar_docs_etsinf
from app.escuelas.etsit_docs import cargar_docs_etsit
from app.escuelas.etsiccp_docs import cargar_docs_etsiccp
from app.escuelas.umu_docs import cargar_docs_umu
import logging

logger = logging.getLogger(__name__)

def _get_embeddings():
    emb_key = os.getenv("OPENAI_EMBEDDINGS_API_KEY")
    emb_base = os.getenv("OPENAI_EMBEDDINGS_BASE_URL")
    normal_key = os.getenv("OPENAI_API_KEY")
    normal_base = os.getenv("OPENAI_BASE_URL")

    logger.warning(f"EMB key visible: {bool(emb_key)}")
    logger.warning(f"EMB base visible: {emb_base}")
    logger.warning(f"NORMAL base: {normal_base}")

    
    return OpenAIEmbeddings(
        model=os.getenv("EMBEDDINGS_MODEL", "text-embedding-3-small"),
        api_key=emb_key or normal_key,
        base_url=emb_base or "https://api.openai.com/v1",
    )





# ==============================
#  Rutas de datos
# ==============================
DATA_DIR = Path(os.getenv("DATA_DIR", Path(__file__).resolve().parent / "Datos")).resolve()



# ============================
# Config
# ============================
EMBEDDINGS_MODEL = os.getenv("EMBEDDINGS_MODEL", "text-embedding-3-small")
INDEX_DIR = os.getenv("FAISS_INDEX_DIR", "/app/faiss_index")  # mapea a volumen en docker-compose
ALLOW_UNSAFE = True  # para load_local en prod con LC >=0.2

# ============================
# Utilidades
# ============================
def _ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)

def _has_faiss_index(path: str) -> bool:
    # FAISS guarda: index.faiss + index.pkl
    return os.path.exists(os.path.join(path, "index.faiss")) and os.path.exists(os.path.join(path, "index.pkl"))



# ==============================
#  Scrapers
# ==============================
def scrape_empresa(url: str, role: str, school: str = "ALL"):
    """
    Extrae secciones de la página de la ETSINF para empresas y devuelve chunks con metadata de rol.
    Conserva los enlaces embebidos (Texto visible + URL).
    """
    headers = {"User-Agent": "Mozilla/5.0 (Jupyter; Python)"}
    resp = requests.get(url, headers=headers, timeout=15)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    raw_docs = []
    for nodo in soup.select("div.wp-block-upv-acordeon"):
        title_el = nodo.select_one("h3")
        title = title_el.get_text(strip=True) if title_el else "Sin título"
        body = nodo.find("div", class_=lambda c: c and ("acordeon__body" in c or "closed" in c))
        if not body:
            continue

        # Convertir <a>texto</a> a "texto (URL)"
        for a in body.find_all("a", href=True):
            link_text = a.get_text(strip=True)
            href = a["href"]
            a.replace_with(f"{link_text} ({href})")

        text = body.get_text("\n", strip=True)
        raw_docs.append(
            Document(
                page_content=f"## {title}\n\n{text}",
                metadata={"source": url, "role": role, "school": school},
            )
        )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=750,
        chunk_overlap=200,
        separators=["\n\n", "\n", " ", ""],
    )
    return splitter.split_documents(raw_docs)


def scrape_estudiante(url: str, role: str, school: str = "ALL"):
    """
    Extrae información general (excepto la tabla) desde la web de estudiante de la ETSINF.
    Conserva enlaces embebidos (Texto visible + URL).
    """
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url, headers=headers, timeout=15)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    main_content = soup.find("div", class_="contenido") or soup.find("main") or soup.body
    if main_content:
        # Evitar duplicar la tabla (la extrae loader)
        for table in main_content.find_all("table"):
            table.decompose()
        for a in main_content.find_all("a", href=True):
            link_text = a.get_text(strip=True)
            href = a["href"]
            a.replace_with(f"{link_text} ({href})")

    raw_text = main_content.get_text("\n", strip=True) if main_content else ""
    doc = Document(
        page_content="## Información adicional sobre prácticas\n\n" + raw_text,
        metadata={"source": url, "role": role, "school": school},
    )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=250,
        separators=["\n\n", "\n", " ", ""],
    )
    return splitter.split_documents([doc])



def _has_faiss_index(path: str) -> bool:
    return (
        os.path.exists(os.path.join(path, "index.faiss")) and
        os.path.exists(os.path.join(path, "index.pkl"))
    )

def _make_id(doc):
    # ID estable por contenido + metadatos clave
    role = doc.metadata.get("role", "")
    school = doc.metadata.get("school", "")
    base = f"{doc.page_content}||{role}||{school}"
    return md5(base.encode("utf-8")).hexdigest()


def construir_o_cargar_indice(ruta_directorio: Optional[str] = None) -> FAISS:
    """Construye o carga el índice FAISS con todos los documentos (PDFs, scrapers y manuales por escuela)."""
    index_dir = ruta_directorio or INDEX_DIR
    os.makedirs(index_dir, exist_ok=True)
   

    embeddings = _get_embeddings()




    index_path = os.path.join(index_dir, "index.faiss")
    metadata_path = os.path.join(index_dir, "index.pkl")

   


    logger.info("Creando nuevo índice FAISS con documentos de la UPV...")

    all_docs: List[Document] = []

    # Normativa general (ALL)
    pdf_estudiante = [
        (str(DATA_DIR / "ReglamPracUPVMod2022.pdf"), "normativa_estudiante.txt")
    ]
    ruta_tabla_estudiante = str(DATA_DIR / "Informacion-Practicas-Externas-ETSINF.pdf")
    pdf_empresa = [
        (str(DATA_DIR / "ReglamPracUPVMod2022.pdf"), "normativa_empresa.txt")
    ]

    docs_est = cargar_documentos_y_tabla(pdf_estudiante, ruta_tabla_pdf=ruta_tabla_estudiante,
                                         role="estudiante", school="ALL", solo_tabla=False)
    docs_est += cargar_chunks_manual(role="estudiante", school="ALL")

    docs_emp = cargar_documentos_y_tabla(pdf_empresa, ruta_tabla_pdf=None,
                                         role="empresa", school="ALL", solo_tabla=False)
    docs_emp += cargar_chunks_manual(role="empresa", school="ALL")

    # Web scraping ETSINF
    docs_emp += scrape_empresa("https://www.upv.es/entidades/etsinf/empresa/", role="empresa", school="ALL")
    docs_est += scrape_estudiante("https://www.upv.es/entidades/etsinf/informacion-estudiante/", role="estudiante", school="ALL")

    # Limpieza textual común
    for doc in docs_emp + docs_est:
        doc.page_content = (
            doc.page_content
            .replace("ETSINF", "UPV")
            .replace("upe_inf@etsinf.upv.es", "la Unidad de Prácticas correspondiente de tu escuela")
            .replace("Escuela Técnica Superior de Ingeniería Informática", "la escuela correspondiente de la UPV")
        )

    all_docs += docs_est + docs_emp

    # Documentos por escuela
    all_docs += cargar_docs_ade()
    all_docs += cargar_docs_bbaa()
    all_docs += cargar_docs_epsa()
    all_docs += cargar_docs_epsg()
    all_docs += cargar_docs_etsa()
    all_docs += cargar_docs_etsiadi()
    all_docs += cargar_docs_etsiamn()
    all_docs += cargar_docs_etsie()
    all_docs += cargar_docs_etsii()
    all_docs += cargar_docs_etsigct()
    all_docs += cargar_docs_etsinf()
    all_docs += cargar_docs_etsit()
    all_docs += cargar_docs_etsiccp()
    all_docs += cargar_docs_umu()

    # Asignar IDs únicos
    seen = set()
    ids = []
    for doc in all_docs:
        base_chk = _make_id(doc)
        unique_id, suf = base_chk, 1
        while unique_id in seen:
            unique_id = f"{base_chk}_{suf}"; suf += 1
        seen.add(unique_id)
        doc.metadata["checksum"] = base_chk
        doc.metadata["id"] = unique_id
        ids.append(unique_id)

    # ------------ carga o crea ------------
    if _has_faiss_index(index_dir):
        logger.info(f"Cargando índice FAISS existente desde {index_dir}")
        try:
            faiss_index = FAISS.load_local(
                index_dir, embeddings=embeddings,
                allow_dangerous_deserialization=True
            )
        except TypeError:
            faiss_index = FAISS.load_local(index_dir, embeddings=embeddings)

        # Estado actual del docstore
        doc_dict = getattr(faiss_index.docstore, "_dict", {}) or {}
        existing_ids = set(doc_dict.keys())
        current_ids = set(ids)

        # Borrados
        to_delete = existing_ids - current_ids
        # Altas
        new_ids = [i for i in ids if i not in existing_ids]

        # Si hay demasiados borrados, más eficiente reconstruir
        if to_delete and len(to_delete) > max(50, int(0.1 * len(existing_ids))):
            logger.warning(f"Muchos borrados ({len(to_delete)}). Reconstruyendo índice completo.")
            faiss_index = FAISS.from_documents(all_docs, embeddings, ids=ids)
        else:
            if to_delete:
                faiss_index.delete(list(to_delete))
                logger.info(f"🗑️ Eliminados {len(to_delete)} chunks obsoletos.")

            if new_ids:
                new_docs = [doc for doc in all_docs if doc.metadata["id"] in new_ids]
                faiss_index.add_documents(new_docs, ids=new_ids)
                logger.info(f"➕ Añadidos {len(new_ids)} nuevos chunks.")

            if not to_delete and not new_ids:
                logger.info("ℹ️ Índice ya está sincronizado. Sin cambios.")

    else:
        logger.info("Creando nuevo índice FAISS con documentos...")
        faiss_index = FAISS.from_documents(all_docs, embeddings, ids=ids)
        logger.info(f"✅ Índice FAISS creado con {len(ids)} chunks.")

    # Guarda
    faiss_index.save_local(index_dir)
    logger.info(f"💾 Índice FAISS guardado en {index_dir}.")
    return faiss_index


if __name__ == "__main__":
    print("Construyendo índice FAISS...")
    construir_o_cargar_indice("practicas_upv")
    print("Índice actualizado correctamente.")