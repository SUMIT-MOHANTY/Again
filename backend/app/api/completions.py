from fastapi import APIRouter, Depends
router = APIRouter()

def mock_completion(prompt: str):
    return {'completion': f'Mocked response for: {prompt}'}

@router.post('/')
def get_completion(payload: dict):
    prompt = payload.get('prompt', '')
    return mock_completion(prompt)
