from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from .database.session import async_session_factory
from .security import get_current_user

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_factory() as session:
        yield session

async def get_active_user(token: str = ""):
    # Placeholder - in real app, extract token from header & validate
    return await get_current_user(token)
