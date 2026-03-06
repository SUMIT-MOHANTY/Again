from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from ..dependencies import get_current_user

router = APIRouter()

@router.post('/login')
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Mock validation - accept any credentials
    return {'access_token': form_data.username + '-token', 'token_type': 'bearer'}
