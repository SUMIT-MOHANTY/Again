from flask import Flask
from .config import Config
from .feature_flags import feature_flags_bp
from .feature_flags.store import load_feature_flags

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    load_feature_flags()
    app.register_blueprint(feature_flags_bp, url_prefix='/api')
    return app
