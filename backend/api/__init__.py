from flask import Blueprint, jsonify, request
from flask_cors import cross_origin

api_bp = Blueprint('api', __name__)

@api_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy', 'message': 'API is running'}), 200

@api_bp.route('/status', methods=['GET'])
def status():
    return jsonify({
        'version': '1.0.0',
        'environment': 'development'
    }), 200
