from flask import Blueprint, request, jsonify
from services.accessibility_validator import AccessibilityValidator

accessibility_bp = Blueprint('accessibility', __name__, url_prefix='/api/v1/accessibility')
validator = AccessibilityValidator()

@accessibility_bp.route('/audit', methods=['GET'])
def audit_page():
    url = request.args.get('url', '')
    html_content = request.args.get('html', '<html></html>')
    result = validator.check_wcag(url, html_content)
    return jsonify(result)

@accessibility_bp.route('/settings', methods=['GET'])
def get_settings():
    return jsonify({'high_contrast': False, 'reduced_motion': False})
