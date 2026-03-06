from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from ..config import settings

async_engine = create_async_engine(settings.POSTGRES_URL, echo=False, future=True)
async_session_factory = async_sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)
