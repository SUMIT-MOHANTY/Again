from flask import request, jsonify, abort
from . import api_v1
from ...schemas.user import (
    UserCreateRequestSchema,
    UserUpdateRequestSchema,
    UserPatchRequestSchema,
    UserResponseSchema,
)

# In‑memory placeholder data store
_USERS = {}
_NEXT_ID = 1

@api_v1.route('/users', methods=['GET'])
def list_users():
    response = {"users": [], "page": 1, "total": 0}
    return jsonify(response), 200

@api_v1.route('/users', methods=['POST'])
def create_user():
    global _NEXT_ID
    data = request.get_json() or {}
    errors = UserCreateRequestSchema().validate(data)
    if errors:
        return jsonify(errors), 400
    user = {
        "id": _NEXT_ID,
        "username": data["username"],
        "email": data["email"],
        "created_at": "2023-01-01T00:00:00Z",
    }
    _USERS[_NEXT_ID] = user
    _NEXT_ID += 1
    return jsonify(UserResponseSchema().dump(user)), 201

@api_v1.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = _USERS.get(user_id)
    if not user:
        abort(404)
    return jsonify(UserResponseSchema().dump(user)), 200

@api_v1.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = _USERS.get(user_id)
    if not user:
        abort(404)
    data = request.get_json() or {}
    errors = UserUpdateRequestSchema().validate(data)
    if errors:
        return jsonify(errors), 400
    user.update({
        "username": data.get("username", user["username"]),
        "email": data.get("email", user["email"]),
    })
    return jsonify(UserResponseSchema().dump(user)), 200

@api_v1.route('/users/<int:user_id>', methods=['PATCH'])
def patch_user(user_id):
    user = _USERS.get(user_id)
    if not user:
        abort(404)
    data = request.get_json() or {}
    errors = UserPatchRequestSchema().validate(data)
    if errors:
        return jsonify(errors), 400
    user.update(data)
    return jsonify(UserResponseSchema().dump(user)), 200

@api_v1.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in _USERS:
        del _USERS[user_id]
    return jsonify({"deleted": True}), 204
