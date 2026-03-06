from fastapi import FastAPI
from .config import settings
from .api import router as api_router

def create_app() -> FastAPI:
    app = FastAPI(title=settings.PROJECT_NAME)
    app.include_router(api_router)
    return app
