from fastapi import FastAPI
from .config import settings
from .api.router import api_router

app = FastAPI(title=settings.PROJECT_NAME)
app.include_router(api_router)
