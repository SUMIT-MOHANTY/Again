from flask import Blueprint

api_bp = Blueprint('api', __name__)

from . import routes

# Register routes
api_bp.add_url_rule('/health', 'health', routes.health, methods=['GET'])
api_bp.add_url_rule('/items', 'items', routes.get_items, methods=['GET'])
