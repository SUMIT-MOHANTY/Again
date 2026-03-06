from fastapi import APIRouter

router = APIRouter()

@router.post('/prompts')
def create_prompt():
    return {'status': 'created'}
