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
import uvicorn
from app import create_app

app = create_app()

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
