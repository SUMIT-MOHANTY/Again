from flask import Flask, jsonify
from backend.health import health_bp
from backend.db import db

def create_app():
    app = Flask(__name__)
    
    # Initialize database
    db.init_app(app)
    
    # Register blueprints
    app.register_blueprint(health_bp)
    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Not found'}), 404
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)
