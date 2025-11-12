import os
from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

# --- Configuración base de datos ---
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./rag_data.db")

engine = create_async_engine(DATABASE_URL, echo=False, future=True)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()

# --- Modelo Feedback ---
class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String(100), nullable=True)
    user_id = Column(String(100), nullable=True)   
    role = Column(String(30), nullable=True)
    question = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)
    feedback = Column(String(10), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


class Conversation(Base):
    __tablename__ = "conversation"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String(100), nullable=True)
    user_id = Column(String(100), nullable=True)   
    role = Column(String(30), nullable=True)
    question = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    school = Column(String, default="ALL")



async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
