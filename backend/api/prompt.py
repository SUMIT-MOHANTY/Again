from flask import Blueprint, request, jsonify
from ..services.prompt_service import process_prompt

bp = Blueprint('prompt', __name__)

@bp.route('/prompt', methods=['POST'])
def handle_prompt():
    data = request.get_json(silent=True) or {}
    prompt = data.get('prompt', '')
    if not prompt:
        return jsonify({'error': 'prompt required'}), 400
    result = process_prompt(prompt)
    return jsonify({'result': result})
