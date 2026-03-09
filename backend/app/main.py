import uvicorn
from . import create_app
from fastapi import FastAPI
from .api import users, prompts, completions

def create_app() -> FastAPI:
    app = FastAPI(title='Analytics Dashboard')
    app.include_router(users.router, prefix='/api/users', tags=['users'])
    app.include_router(prompts.router, prefix='/api/prompts', tags=['prompts'])
    app.include_router(completions.router, prefix='/api/completions', tags=['completions'])
    return app

if __name__ == "__main__":
    uvicorn.run("backend.app.main:app", host="0.0.0.0", port=8000, reload=True)
app = create_app()
