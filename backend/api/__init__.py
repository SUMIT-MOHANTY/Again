from flask import Blueprint

def create_seo_bp(seo_service):
    bp = Blueprint('seo', __name__, url_prefix='/api/v1/seo')
    @bp.route('/analyze', methods=['GET'])
    def analyze():
        url = 'http://example.com'  # Mock
        return seo_service.analyze(url, {'title': 'Test', 'description': 'Test desc', 'og:title': 'Test'})
    return bp

def create_a11y_bp(a11y_service):
    bp = Blueprint('accessibility', __name__, url_prefix='/api/v1/accessibility')
    @bp.route('/audit', methods=['GET'])
    def audit():
        return a11y_service.check_wcag('http://example.com', '<html></html>')
    return bp
