from fastapi import FastAPI
from .api import router as api_router
from .models.base import Base
from .dependencies import engine

def create_app() -> FastAPI:
    app = FastAPI(title='Staging API')
    app.include_router(api_router)
    # Create tables on startup (for staging/mock)
    @app.on_event('startup')
    def on_startup():
        Base.metadata.create_all(bind=engine)
    return app

app = create_app()
