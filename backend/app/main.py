from fastapi import FastAPI
from .api import users, prompts, completions

def create_app() -> FastAPI:
    app = FastAPI(title='Analytics Dashboard')
    app.include_router(users.router, prefix='/api/users', tags=['users'])
    app.include_router(prompts.router, prefix='/api/prompts', tags=['prompts'])
    app.include_router(completions.router, prefix='/api/completions', tags=['completions'])
    return app

app = create_app()
