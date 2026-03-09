from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
import os

POSTGRES_DSN = os.getenv("POSTGRES_DSN", "postgresql+asyncpg://user:pass@localhost:5432/db")
engine = create_async_engine(POSTGRES_DSN, echo=False, future=True)
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
