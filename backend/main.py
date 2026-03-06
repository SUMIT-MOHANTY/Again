import os
from fastapi import FastAPI
from .routers import book

app = FastAPI(title="Book Service with Redis Cache")
app.include_router(book.router)

@app.on_event("startup")
async def startup():
    # Ensure tables exist - in production use migrations
    from .database import engine, Base
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
