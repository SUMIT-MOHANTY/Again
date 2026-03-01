from flask import Flask
from flask_cors import CORS
from backend.models import db
from backend.extensions import jwt
from backend.api import auth_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auth.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'super-secret-key'
    
    db.init_app(app)
    jwt.init_app(app)
    CORS(app, origins=['http://localhost:3000'])
    
    app.register_blueprint(auth_bp)
    
    with app.app_context():
        db.create_all()
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=5000, debug=True)
