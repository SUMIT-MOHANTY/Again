from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from api import auth_bp
from api.models import db
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    CORS(app)
    db.init_app(app)
    jwt = JWTManager(app)
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    
    with app.app_context():
        db.create_all()
    
    return app

if __name__ == '__main__':
    create_app().run(host='0.0.0.0', port=5000)
