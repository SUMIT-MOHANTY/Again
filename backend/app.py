from flask import Flask
from flask_cors import CORS
from models import db
from config import Config
from api.routes import seo, accessibility

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    CORS(app)
    db.init_app(app)

    app.register_blueprint(seo.seo_bp)
    app.register_blueprint(accessibility.accessibility_bp)

    @app.route('/health')
    def health():
        return {'status': 'healthy'}

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)
