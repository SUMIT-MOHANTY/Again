import os

class Settings:
    PROJECT_NAME = os.getenv('PROJECT_NAME', 'AccessibilityApp')
    DEBUG = os.getenv('DEBUG', 'false').lower() == 'true'

settings = Settings()
