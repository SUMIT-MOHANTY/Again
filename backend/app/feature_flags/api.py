from flask import Blueprint, request, jsonify, abort
from .store import FEATURE_FLAGS
from .models import FeatureFlag

feature_flags_bp = Blueprint('feature_flags', __name__)

def _admin_required():
    if not request.headers.get('X-Admin'):
        abort(403)

@feature_flags_bp.route('/flags', methods=['GET'])
def get_flags():
    _admin_required()
    result = [{'name': f.name, 'enabled': f.enabled, 'description': f.description}
              for f in FEATURE_FLAGS.values()]
    return jsonify(result)

@feature_flags_bp.route('/flags/<name>', methods=['POST'])
def toggle_flag(name):
    _admin_required()
    payload = request.get_json(silent=True) or {}
    enabled = payload.get('enabled')
    description = payload.get('description', '')
    if enabled is None:
        abort(400, '"enabled" field required')
    flag = FEATURE_FLAGS.get(name)
    if flag:
        flag.enabled = bool(enabled)
        flag.description = description
    else:
        FEATURE_FLAGS[name] = FeatureFlag(name, bool(enabled), description)
    return jsonify({'name': name, 'enabled': bool(enabled), 'description': description})
