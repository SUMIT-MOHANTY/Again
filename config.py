import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key')
    
    # SMTP Settings
    SMTP_HOST = os.environ.get('SMTP_HOST', 'localhost')
    SMTP_PORT = int(os.environ.get('SMTP_PORT', 1025))
    SMTP_USER = os.environ.get('SMTP_USER', '')
    SMTP_PASSWORD = os.environ.get('SMTP_PASSWORD', '')
    SMTP_FROM_EMAIL = os.environ.get('SMTP_FROM_EMAIL', 'noreply@portfolio.local')
    
    # Admin email
    ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL', 'admin@portfolio.local')
    
    # Frontend URL for CORS
    FRONTEND_URL = os.environ.get('FRONTEND_URL', 'http://localhost:3000')
    
    # Development mode (mock SMTP)
    DEBUG = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
