from fastapi import FastAPI
from .api.v1.flag_routes import router as flag_router

def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(flag_router)
    return app
