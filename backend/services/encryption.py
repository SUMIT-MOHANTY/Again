from cryptography.fernet import Fernet, InvalidToken
from ..config import settings

_fernet = Fernet(settings.ENCRYPTION_KEY.encode())

def encrypt_value(plain: str) -> bytes:
    return _fernet.encrypt(plain.encode())

def decrypt_value(cipher: bytes) -> str:
    try:
        return _fernet.decrypt(cipher).decode()
    except InvalidToken as exc:
        raise ValueError('Decryption failed') from exc
