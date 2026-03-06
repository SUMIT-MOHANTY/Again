from flask import jsonify, request, current_app
from . import bp
@bp.route('/health', methods=['GET'])
def health():
    return jsonify({'status':'ok'}), 200

@bp.route('/test', methods=['GET'])
def test_resource():
    # Example protected endpoint
    return jsonify({
        'message':'success',
        'user_agent': request.headers.get('User-Agent')
    }), 200
