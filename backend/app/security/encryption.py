import os

def get_encryption_key() -> bytes:
    return os.getenv('ENCRYPTION_KEY', 'your-key-here').encode()
