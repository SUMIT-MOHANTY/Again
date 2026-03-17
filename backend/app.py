from flask import Flask, jsonify
from flask_cors import CORS
from backend.health import health_bp
from backend.db import db
from config import Config
from api.routes import seo, accessibility

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    CORS(app)
    db.init_app(app)
    
    # Register blueprints
    app.register_blueprint(health_bp)
    app.register_blueprint(seo.seo_bp)
    app.register_blueprint(accessibility.accessibility_bp)
    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Not found'}), 404
    
    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)
