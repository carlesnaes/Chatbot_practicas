import os
import time
from unittest import result
import yaml
from loguru import logger
from typing import List, Dict, Optional

import app.indexador

#  Imports clásicos 
from langchain.chains import ConversationalRetrievalChain
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferWindowMemory
from langchain.retrievers import ContextualCompressionRetriever
from langchain.prompts import PromptTemplate

from langchain.schema import AIMessage
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import asyncio

from app.db import AsyncSessionLocal, Conversation
from sqlalchemy.future import select
from langchain.memory import ConversationBufferWindowMemory
from app.indexador import construir_o_cargar_indice





# ============================
# Config
# ============================
CHAT_MODEL_NAME   = os.getenv("CHAT_MODEL_NAME", "gpt-4o-mini")
TEMPERATURE       = float(os.getenv("CHAT_TEMPERATURE", "0.2"))
MMR_K             = int(os.getenv("MMR_K", "15"))
MMR_FETCH_K       = int(os.getenv("MMR_FETCH_K", "50"))
MMR_LAMBDA        = float(os.getenv("MMR_LAMBDA", "0.5"))
RERANKER_MODEL    = os.getenv("RERANKER_MODEL_NAME", "BAAI/bge-reranker-base")
COMPRESSION_TOP_N = int(os.getenv("COMPRESSION_TOP_N", "15"))
CONTEXT_WINDOW_SIZE = int(os.getenv("CONTEXT_WINDOW_SIZE", "4"))

PROMPTS_PATH      = os.getenv("PROMPTS_PATH", "/app/Prompts/prompts.yaml")
FAISS_INDEX_DIR   = os.getenv("FAISS_INDEX_DIR", "/app/faiss_index")

# ============================
# Prompt loader
# ============================

def build_prompt_from_yaml(role: str, school: str = "ALL") -> PromptTemplate:
    """
    Devuelve un PromptTemplate con los placeholders {context} y {question}.
    """
    import os, yaml
    from loguru import logger

    here = os.path.dirname(__file__)
    yaml_path = os.path.join(here, "Prompts", "prompts.yaml")
    with open(yaml_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    prompts = data.get("prompts", [])

    def _get(name):
        return next((p.get("template") for p in prompts if p.get("name") == name), None)

    primary = f"estricto_{role}_{school}"
    template = _get(primary)
    if not template:
        fallback = f"estricto_{role}_ALL"
        template = _get(fallback)
        if template:
            logger.warning(f"⚠️ No existe '{primary}', usando fallback '{fallback}'.")
        else:
            raise ValueError(f"No se encontró '{primary}' ni '{fallback}' en prompts.yaml")

    #  Devolver PromptTemplate
    return PromptTemplate(
        input_variables=["context", "question"],
        template=template
    )


# ============================
# Memoria conversacional
# ============================
def get_memory():
    return ConversationBufferWindowMemory(
        memory_key="chat_history",
        return_messages=True,
        output_key="answer",
        k=CONTEXT_WINDOW_SIZE
    )

# ============================
# Cadenas RAG
# ============================
# def crear_rag_chain(vectorstore, memory, prompt_template: str, role: str, school: str = "ALL"):
#     """
#     Crea una ConversationalRetrievalChain con reranker BGE.
#     """
#     llm = ChatOpenAI(model=CHAT_MODEL_NAME, temperature=TEMPERATURE)

#     #  Cross-encoder (para rerank)
#     reranker = HuggingFaceCrossEncoder(model_name=RERANKER_MODEL)
#     compressor = CrossEncoderReranker(model=reranker, top_n=COMPRESSION_TOP_N)

#     filtros = {
#         "role": role,
#         "school": {"$in": [school, "ALL"]}
#     }

#     base_retriever = vectorstore.as_retriever(
#         search_type="mmr",
#         search_kwargs={
#             "k": MMR_K,
#             "fetch_k": MMR_FETCH_K,
#             "lambda_mult": MMR_LAMBDA,
#             "filter": filtros,
#             "score": True
#         }
#     )

#     compression_retriever = ContextualCompressionRetriever(
#         base_retriever=base_retriever,
#         base_compressor=compressor
#     )

#     chain = ConversationalRetrievalChain.from_llm(
#         llm=llm,
#         retriever=compression_retriever,
#         memory=memory,
#         return_source_documents=True,
#         output_key="answer",
#         combine_docs_chain_kwargs={"prompt": prompt_template}
#     )

#     return chain


def _build_filters(role: str, school: str) -> dict:
   
    if school == "ALL":
        return {"role": role, "school": "ALL"}
    else:
        return {"role": role, "school": school}


def crear_rag_chain_sin_reranker(vectorstore, memory, prompt_template: str, role: str, school: str = "ALL"):
    """
    Versión sin reranker (sólo MMR retriever)
    """
    llm = ChatOpenAI(model=CHAT_MODEL_NAME, temperature=TEMPERATURE)

    filtros = _build_filters(role, school)



    retriever = vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": MMR_K,
            "fetch_k": MMR_FETCH_K,
            "lambda_mult": MMR_LAMBDA,
            "filter": filtros,
            "score": True
        }
    )

    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        return_source_documents=True,
        output_key="answer",
        combine_docs_chain_kwargs={"prompt": prompt_template}
    )

    return chain

# ============================
# Vectorstore
# ============================


FAISS_INDEX_DIR   = os.getenv("FAISS_INDEX_DIR", "/app/faiss_index")
_VECTORSTORE = None  # caché en memoria

def get_vectorstore(force: bool = False):
    global _VECTORSTORE

    if force:
        print("🌀 Forzando reconstrucción completa del índice FAISS...")
        _VECTORSTORE = None  
        _VECTORSTORE = construir_o_cargar_indice(FAISS_INDEX_DIR)
        return _VECTORSTORE

    if _VECTORSTORE is None:
        _VECTORSTORE = construir_o_cargar_indice(FAISS_INDEX_DIR)
    return _VECTORSTORE



async def build_memory_from_db(session_id: str, role: str = None, school: str = None):
    memory = ConversationBufferWindowMemory(
        memory_key="chat_history",
        return_messages=True,
        output_key="answer"
    )

    async with AsyncSessionLocal() as db:
        query = select(Conversation).where(Conversation.session_id == session_id)
        if role:
            query = query.filter(Conversation.role == role)
        if school and school != "ALL":
            query = query.filter(Conversation.answer.ilike(f"%{school}%"))  # opcional
        query = query.order_by(Conversation.created_at.asc())
        result = await db.execute(query)
        rows = result.scalars().all()

    for r in rows:
        memory.chat_memory.add_user_message(r.question)
        memory.chat_memory.add_ai_message(r.answer)

    logger.info(f" Memoria reconstruida: {len(rows)} turnos previos (role={role}, school={school})")
    return memory



# ============================
# Pipeline principal
# ============================
async def generate_answer(query: str, role: str, school: str, session_id: str, vectorstore=None):
    from langchain.schema import Document
    import difflib

    role = (role or "").strip().lower()
    school = (school or "ALL").strip().upper()
    if vectorstore is None:
        vectorstore = get_vectorstore()

    #  Cargar memoria real desde la BD (persistente)
    try:
        memory = await build_memory_from_db(session_id, role, school)
    except Exception as e:
        logger.warning(f"⚠️ No se pudo reconstruir la memoria desde DB ({e}), usando memoria vacía.")
        memory = get_memory()

    prompt = build_prompt_from_yaml(role, school)
    rag = crear_rag_chain_sin_reranker(vectorstore, memory, prompt, role, school)
    result = rag({"question": query})
    # ---  Fallback si no se han recuperado documentos ---
    

    def pack_sources(res):
        return [
            {
                "source": doc.metadata.get("source", "sin fuente"),
                "role": doc.metadata.get("role", "N/A"),
                "school": doc.metadata.get("school", "N/A"),
                "preview": (doc.page_content[:400].replace("\n", " ") + "...") if getattr(doc, "page_content", "") else "..."
            }
            for doc in res.get("source_documents", []) or []
        ]

    answer = (result.get("answer") or "").strip()
    sources = pack_sources(result)
    if not result.get("source_documents"):
        logger.warning(f"⚠️ Sin documentos encontrados para {school}. Activando fallback a ALL.")
        if role != "empresa" and school != "ALL":
            prompt_all = build_prompt_from_yaml(role, "ALL")
            rag_all = crear_rag_chain_sin_reranker(vectorstore, memory, prompt_all, role, "ALL")
            result_all = rag_all({"question": query})
            answer = (result_all.get("answer") or "").strip()
            sources = pack_sources(result_all)
            return answer, sources


    # --- Detección de evasivas ---
    frases_evasivas = [
        "no tengo esa información",
        "no se especifica",
        "no aparece en la normativa",
        "no está indicado",
        "no figura",
        "no dispongo de esa información",
        "no lo sé",
        "la normativa proporcionada no especifica",
        "no hay información disponible",
        "no consta",
        "no está contemplado",
        "no se menciona",
        "no se indica",
        "no hay datos",
        "no puedo responder",
        "no se puede responder",
        "La normativa de la Universitat Politècnica de València (UPV) no especifica"
    ]
    logger.info(f" Docs recuperados antes del modelo: {len(result.get('source_documents', []))}")

    def es_respuesta_evasiva(texto: str, umbral_similitud: float = 0.80) -> bool:
        texto = texto.lower().strip()
        frases_respuesta = texto.split(".")
        for ref in frases_evasivas:
            ref = ref.lower().strip()
            for fragmento in frases_respuesta:
                similitud = difflib.SequenceMatcher(None, fragmento.strip(), ref).ratio()
                if similitud > umbral_similitud or ref in fragmento:
                    return True
        return False

    respuesta_evasiva = es_respuesta_evasiva(answer)

    # --- Fallback ---
    if role != "empresa" and school != "ALL" and respuesta_evasiva:
        logger.warning(f"⚠️ Fallback activado (respuesta evasiva detectada en {school})")
        prompt_all = build_prompt_from_yaml(role, "ALL")
        rag_all = crear_rag_chain_sin_reranker(vectorstore, memory, prompt_all, role, "ALL")
        result_all = rag_all({"question": query})
        answer = (result_all.get("answer") or "").strip()
        sources = pack_sources(result_all)

    return answer, sources



