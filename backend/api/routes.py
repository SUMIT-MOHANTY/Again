from flask import Blueprint, request, jsonify
from backend.api.schemas import PortfolioResponse, PortfolioItem
from backend.services.portfolio_service import search_portfolios
from backend.data.mock_data import load_mock_data

portfolio_bp = Blueprint('portfolio', __name__)

@portfolio_bp.before_app_request
def load_data():
    from flask import current_app
    from backend.models import db
    with current_app.app_context():
        load_mock_data()

@portfolio_bp.route('/portfolio', methods=['GET'])
def search_portfolio():
    query = request.args.get('q', '')
    category = request.args.get('category', '')
    tags = request.args.get('tags', '')
    tag_list = tags.split(',') if tags else []
    results = search_portfolios(query, category, tag_list)
    items = [PortfolioItem(
        id=p.id,
        title=p.title,
        description=p.description,
        category=p.category.name if p.category else '',
        technologies=[t.name for t in p.technologies],
        image_url=p.image_url,
        project_url=p.project_url
    ) for p in results]
    return jsonify(PortfolioResponse(items=items, total=len(items)).model_dump())
