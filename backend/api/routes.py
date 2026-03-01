from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from .models import db, User
from utils import generate_token, validate_register, validate_login

auth_bp = Blueprint('auth_bp', __name__)

# Token blocklist for logout
token_blocklist = set()

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    errors = validate_register(data)
    if errors:
        return jsonify({'error': errors[0]}), 400
    
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'error': 'Username already exists'}), 409
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Email already exists'}), 409
    
    user = User(username=data['username'], email=data['email'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    
    return jsonify({'message': 'User registered successfully', 'user': user.to_dict()}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    errors = validate_login(data)
    if errors:
        return jsonify({'error': errors[0]}), 400
    
    user = User.query.filter_by(email=data['email']).first()
    if not user or not user.check_password(data['password']):
        return jsonify({'error': 'Invalid credentials'}), 401
    
    token = generate_token(user.id)
    return jsonify({'access_token': token, 'token_type': 'Bearer', 'user': user.to_dict()}), 200

@auth_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    jti = get_jwt()['jti']
    token_blocklist.add(jti)
    return jsonify({'message': 'Successfully logged out'}), 200

@auth_bp.route('/me', methods=['GET'])
@jwt_required()
def get_current_user():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user.to_dict()), 200

@auth_bp.route('/refresh', methods=['POST'])
@jwt_required()
def refresh():
    user_id = get_jwt_identity()
    new_token = generate_token(user_id)
    return jsonify({'access_token': new_token, 'token_type': 'Bearer'}), 200
