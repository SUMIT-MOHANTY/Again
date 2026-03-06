from flask import Blueprint, request, jsonify
from . import db
from .models import Role, Permission, User
from .middleware import rbac_required
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

api_bp = Blueprint('api', __name__)

# ----- Auth -----
@api_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data.get('username')).first()
    if not user or not user.password_hash == data.get('password'):
        return jsonify({'msg': 'Bad credentials'}), 401
    # Collect permissions from roles
    perms = []
    for role in user.roles:
        for p in role.permissions:
            perms.append(f"{p.action}:{p.resource}")
    additional_claims = {'permissions': perms}
    access_token = create_access_token(identity=user.id, additional_claims=additional_claims)
    return jsonify(access_token=access_token)

# ----- Role Management -----
@api_bp.route('/roles', methods=['POST'])
@jwt_required()
@rbac_required('create', 'role')
def create_role():
    data = request.json
    role = Role(name=data['name'])
    db.session.add(role)
    db.session.commit()
    return jsonify({'msg': 'role created', 'id': role.id})

@api_bp.route('/roles/<int:role_id>', methods=['GET'])
@jwt_required()
@rbac_required('read', 'role')
def get_role(role_id):
    role = Role.query.get_or_404(role_id)
    perms = [{'action': p.action, 'resource': p.resource} for p in role.permissions]
    return jsonify({'id': role.id, 'name': role.name, 'permissions': perms})

# ----- Permission Management -----
@api_bp.route('/permissions', methods=['POST'])
@jwt_required()
@rbac_required('create', 'permission')
def create_permission():
    data = request.json
    perm = Permission(action=data['action'], resource=data['resource'])
    db.session.add(perm)
    db.session.commit()
    return jsonify({'msg': 'permission created', 'id': perm.id})
