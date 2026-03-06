from fastapi import APIRouter, HTTPException
router = APIRouter()

@router.get('/')
def list_users():
    return [{'id': 1, 'username': 'demo'}]
