from fastapi import APIRouter
router = APIRouter()

@router.post('/')
def create_prompt(prompt: dict):
    return {'id': 1, **prompt}
