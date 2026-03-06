import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_URL = os.getenv('DATABASE_URL', 'postgresql+psycopg2://postgres:postgres@db:5432/postgres')
JWT_SECRET = os.getenv('JWT_SECRET', 'super-secret-key')
ENCRYPTION_KEY = os.getenv('ENCRYPTION_KEY', 'your-key-here')
# Ensure Fernet key size (32 url‑safe base64 bytes)
if len(ENCRYPTION_KEY) < 32:
    ENCRYPTION_KEY = ENCRYPTION_KEY.ljust(32, '0')
FERNET_KEY = base64.urlsafe_b64encode(ENCRYPTION_KEY.encode())
