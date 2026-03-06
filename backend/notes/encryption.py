from cryptography.fernet import Fernet
from ..config import FERNET_KEY

_f = Fernet(FERNET_KEY)

def encrypt(plain: str) -> str:
    if plain is None:
        return None
    return _f.encrypt(plain.encode()).decode()

def decrypt(token: str) -> str:
    if token is None:
        return None
    return _f.decrypt(token.encode()).decode()
