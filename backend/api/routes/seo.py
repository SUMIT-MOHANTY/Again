from flask import Blueprint, request, jsonify
from services.seo_analyzer import SEOAnalyzer

seo_bp = Blueprint('seo', __name__, url_prefix='/api/v1/seo')
seo_analyzer = SEOAnalyzer()

@seo_bp.route('/analyze', methods=['GET'])
def analyze_page():
    url = request.args.get('url', '')
    data = {
        'title': request.args.get('title', ''),
        'description': request.args.get('description', ''),
        'og:title': request.args.get('og_title', ''),
        'og:description': request.args.get('og_description', ''),
        'og:image': request.args.get('og_image', ''),
    }
    result = seo_analyzer.analyze(url, data)
    return jsonify(result)

@seo_bp.route('/pages', methods=['GET'])
def list_pages():
    return jsonify({'pages': []})  # Mock
