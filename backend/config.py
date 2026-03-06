import os
class Config:
    DEBUG = os.getenv('FLASK_DEBUG','false').lower() == 'true'
    TESTING = os.getenv('FLASK_TESTING','false').lower() == 'true'
    SECRET_KEY = os.getenv('SECRET_KEY','change-me')
    # Rate limit settings (requests per window)
    RATE_LIMIT = int(os.getenv('RATE_LIMIT','5'))
    RATE_WINDOW = int(os.getenv('RATE_WINDOW','60'))  # seconds
    # Redis connection URL
    REDIS_URL = os.getenv('REDIS_URL','redis://localhost:6379/0')
    # SQLAlchemy (optional)
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL','sqlite:///./app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
