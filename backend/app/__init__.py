from fastapi import FastAPI
from .config import settings
from .database import Base, engine
from .api import router_user, router_book, router_review

def create_app() -> FastAPI:
    app = FastAPI(title="Library Management Service", version="0.1.0")
    app.include_router(router_user.router)
    app.include_router(router_book.router)
    app.include_router(router_review.router)
    return app
