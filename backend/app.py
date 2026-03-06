from flask import Flask
from .middleware.versioning import versioning_middleware
from .api.v1 import api_v1

def create_app():
    app = Flask(__name__)
    app.wsgi_app = versioning_middleware(app.wsgi_app)
    app.register_blueprint(api_v1)
    return app
