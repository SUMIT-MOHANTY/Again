from flask import Flask
from flask_restx import Api
from flask_cors import CORS
from config import Config

# Initialize email service
email_service = None

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Configure CORS
    CORS(app, resources={
        r"/api/*": {
            "origins": config_class.FRONTEND_URL,
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"]
        }
    })
    
    # Initialize API
    api = Api(app, version='1.0', title='Portfolio API', description='Portfolio Management System API')
    
    # Import and register namespaces
    from app.api.contact import api as contact_ns
    api.add_namespace(contact_ns, path='/api/contact')
    
    # Initialize email service
    global email_service
    from app.services.email_service import EmailService
    email_service = EmailService(config_class)
    
    return app
