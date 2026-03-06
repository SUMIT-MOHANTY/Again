from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import DB_URL

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from .auth.routes import auth_bp
    from .notes.routes import notes_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(notes_bp, url_prefix='/notes')

    @app.route('/')
    def health():
        return {'status': 'ok'}

    return app
