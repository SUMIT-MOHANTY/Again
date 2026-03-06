from fastapi import APIRouter

router = APIRouter()

@router.get('/completions')
def get_completions():
    return []
