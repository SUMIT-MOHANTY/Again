from flask import request, jsonify
from . import api_v1
from ...schemas.auth import LoginRequestSchema, AuthResponseSchema

@api_v1.route('/auth/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    errors = LoginRequestSchema().validate(data)
    if errors:
        return jsonify(errors), 400
    # Dummy token generation for illustration
    token = {"access_token": "dummy-token", "token_type": "Bearer"}
    return jsonify(AuthResponseSchema().dump(token)), 200
