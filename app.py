import os
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
    
    # Register blueprints here when backend modules are ready
    # from backend.api import api_bp
    # app.register_blueprint(api_bp, url_prefix='/api/v1')
    
    @app.route('/api/v1/health')
    def health_check():
        return {'status': 'healthy', 'service': 'flask-api'}
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
