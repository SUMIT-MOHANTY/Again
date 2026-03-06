import os

class Config:
    SECRET_KEY = os.getenv('RBAC_SECRET', 'your-rbac-secret')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@db:5432/rbac')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET', 'jwt-secret-key')
