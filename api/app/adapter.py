from typing import List, Dict, Any, Tuple
from app.rag_chain import generate_answer
from langchain.memory import ConversationBufferWindowMemory
from app.db import AsyncSessionLocal, Conversation
from sqlalchemy.future import select

# LangChain se inicializa dentro de generate_answer()
_retriever = None

async def init_rag() -> None:
    """Inicializa el sistema RAG al arrancar FastAPI."""
    print(" RAG inicializado correctamente (modo sin retriever global).")

async def chat_with_rag(query: str, role: str, school: str, session_id: str):
    answer, sources = await generate_answer(query, role, school, session_id)
    return answer, sources





