from fastapi import FastAPI
from .api import router as api_router

def create_app() -> FastAPI:
    app = FastAPI(title="AI Prompt Service")
    app.include_router(api_router)
    return app
