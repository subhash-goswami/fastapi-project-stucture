from typing import Any, AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base
from src.app.config import settings

# Async engine for PostgreSQL
engine = create_async_engine(settings.DATABASE_URL, echo=True)

# Session factory
async_session = async_sessionmaker(bind=engine, expire_on_commit=False)

# Base class for all models
Base = declarative_base()

# Dependency for FastAPI
async def get_db() -> AsyncGenerator[AsyncSession, Any]:
    async with async_session() as session:
        yield session