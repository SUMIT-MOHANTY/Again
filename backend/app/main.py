from fastapi import FastAPI
from .api import api_router

def create_app() -> FastAPI:
    app = FastAPI(title="Book API")
    app.include_router(api_router, prefix="/api")
    return app

app = create_app()
