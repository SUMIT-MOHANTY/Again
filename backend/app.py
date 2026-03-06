from flask import Flask
from .config import Config
from .api import bp as api_bp
from .middleware.rate_limiter import RateLimiter
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    # Register middleware
    RateLimiter(app)
    # Register blueprints
    app.register_blueprint(api_bp, url_prefix='/api')
    # Global error handler for unexpected errors
    @app.errorhandler(Exception)
    def handle_exception(e):
        return {'error': str(e)}, 500
    return app
