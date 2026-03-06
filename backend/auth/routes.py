from flask import Blueprint, request, jsonify, current_app
import jwt
from datetime import datetime, timedelta
from ..models.user import User
from .. import db
from ..config import JWT_SECRET

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json() or {}
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'msg': 'Missing fields'}), 400
    if User.query.filter_by(username=username).first():
        return jsonify({'msg': 'User exists'}), 400
    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'msg': 'User created'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    username = data.get('username')
    password = data.get('password')
    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        return jsonify({'msg': 'Bad credentials'}), 401
    payload = {
        'sub': user.id,
        'exp': datetime.utcnow() + timedelta(hours=2)
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm='HS256')
    return jsonify({'access_token': token})

def jwt_required(fn):
    def wrapper(*args, **kwargs):
        auth = request.headers.get('Authorization', '')
        parts = auth.split()
        if len(parts) != 2 or parts[0].lower() != 'bearer':
            return jsonify({'msg': 'Missing token'}), 401
        token = parts[1]
        try:
            payload = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
            request.user_id = payload['sub']
        except jwt.ExpiredSignatureError:
            return jsonify({'msg': 'Token expired'}), 401
        except Exception:
            return jsonify({'msg': 'Invalid token'}), 401
        return fn(*args, **kwargs)
    wrapper.__name__ = fn.__name__
    return wrapper
