from sqlalchemy.orm import Session
from ..models.user import User
from ..services.encryption import encrypt_value, decrypt_value

def create_user(db: Session, *, name: str, email: str, ssn: str | None = None) -> User:
    enc_ssn = encrypt_value(ssn) if ssn else None
    db_user = User(name=name, email=email, encrypted_ssn=enc_ssn)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, *, user_id: int, name: str | None = None, email: str | None = None, ssn: str | None = None) -> User:
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise ValueError('User not found')
    if name is not None:
        user.name = name
    if email is not None:
        user.email = email
    if ssn is not None:
        user.encrypted_ssn = encrypt_value(ssn)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_id(db: Session, user_id: int) -> User | None:
    return db.query(User).filter(User.id == user_id).first()

def get_decrypted_ssn(user: User) -> str | None:
    return decrypt_value(user.encrypted_ssn) if user.encrypted_ssn else None
