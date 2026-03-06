import os

class Config:
    DEBUG = os.getenv('FLASK_DEBUG', 'false').lower() == 'true'
    CERT_PATH = os.getenv('CERT_PATH', './certs/placeholder.crt')
    KEY_PATH = os.getenv('KEY_PATH', './certs/placeholder.key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///./data.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
