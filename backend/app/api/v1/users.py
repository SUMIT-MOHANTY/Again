from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..dependencies import get_db, get_current_active_user
from ...schemas.user import UserCreate, UserRead
from ...models.user import User

router = APIRouter()

@router.post('/', response_model=UserRead)
def create_user(user_in: UserCreate, db: Session = Depends(get_db)):
    db_user = User(email=user_in.email, hashed_password=user_in.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get('/me', response_model=UserRead)
def read_me(current_user: User = Depends(get_current_active_user)):
    return current_user
