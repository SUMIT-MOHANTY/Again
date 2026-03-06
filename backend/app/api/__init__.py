from fastapi import APIRouter
from .v1 import auth, users, items

router = APIRouter(prefix='/api/v1')
router.include_router(auth.router, tags=['auth'])
router.include_router(users.router, tags=['users'])
router.include_router(items.router, tags=['items'])
