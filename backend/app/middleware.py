from flask import request, jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_claims
from functools import wraps

def rbac_required(action, resource):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt_claims()
            perms = claims.get('permissions', [])
            needed = f"{action}:{resource}"
            if needed not in perms:
                return jsonify({'msg': 'Forbidden'}), 403
            return fn(*args, **kwargs)
        return wrapper
    return decorator
