from flask import Blueprint, request, jsonify
from ..models.user import User
from .models import Note
from .. import db
from .encryption import encrypt, decrypt
from ..auth.routes import jwt_required

notes_bp = Blueprint('notes', __name__)

@notes_bp.route('', methods=['POST'])
@jwt_required
def create_note():
    data = request.get_json() or {}
    content = data.get('content')
    if content is None:
        return jsonify({'msg': 'Content required'}), 400
    note = Note(user_id=request.user_id)
    note.content = content
    db.session.add(note)
    db.session.commit()
    return jsonify(note.to_dict()), 201

@notes_bp.route('/<int:note_id>', methods=['GET'])
@jwt_required
def get_note(note_id):
    note = Note.query.filter_by(id=note_id, user_id=request.user_id).first()
    if not note:
        return jsonify({'msg': 'Not found'}), 404
    return jsonify(note.to_dict())

@notes_bp.route('/<int:note_id>', methods=['PUT'])
@jwt_required
def update_note(note_id):
    note = Note.query.filter_by(id=note_id, user_id=request.user_id).first()
    if not note:
        return jsonify({'msg': 'Not found'}), 404
    data = request.get_json() or {}
    content = data.get('content')
    if content is not None:
        note.content = content
    db.session.commit()
    return jsonify(note.to_dict())

@notes_bp.route('/<int:note_id>', methods=['DELETE'])
@jwt_required
def delete_note(note_id):
    note = Note.query.filter_by(id=note_id, user_id=request.user_id).first()
    if not note:
        return jsonify({'msg': 'Not found'}), 404
    db.session.delete(note)
    db.session.commit()
    return '', 204
