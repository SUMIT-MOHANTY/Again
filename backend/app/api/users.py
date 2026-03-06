from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..schemas.user import UserCreate, UserRead
from ..models.user import User
from ..db import get_db
from ..services.auth import hash_password, verify_password, create_jwt
import redis, os, secrets, time

router = APIRouter()

# Redis client (simple placeholder, no connection pooling)
redis_client = redis.Redis.from_url(os.getenv("REDIS_URL", "redis://redis:6379/0"))

@router.post("/register", response_model=UserRead)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    db_user = User(email=user.email, hashed_password=hash_password(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    # generate temporary 2FA token
    temp_token = secrets.token_urlsafe(16)
    key = f"2fa:{temp_token}"
    redis_client.setex(key, 300, user.id)  # 5‑minute TTL
    return {"2fa_token": temp_token}

@router.post("/verify-2fa")
def verify_2fa(token: str, code: str, db: Session = Depends(get_db)):
    key = f"2fa:{token}"
    user_id = redis_client.get(key)
    if not user_id:
        raise HTTPException(status_code=400, detail="Invalid or expired 2FA token")
    # mock TOTP verification using the secret from settings
    expected = settings.TWO_FA_SECRET[-6:]  # placeholder logic
    if code != expected:
        raise HTTPException(status_code=401, detail="Invalid 2FA code")
    # generate JWT for authenticated session
    jwt = create_jwt({"sub": int(user_id)})
    redis_client.delete(key)
    return {"access_token": jwt, "token_type": "bearer"}
