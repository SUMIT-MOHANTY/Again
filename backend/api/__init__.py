from flask import Blueprint
from backend.api.routes import portfolio_bp

api_bp = Blueprint('api', __name__)
api_bp.register_blueprint(portfolio_bp)
