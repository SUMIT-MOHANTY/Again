import os
class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    REDIS_URL = os.getenv('REDIS_URL', 'redis://redis:6379/0')
