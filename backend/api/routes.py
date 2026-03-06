from . import api_bp
from flask import jsonify, request, current_app
from ..models import db, BackupLog
@api_bp.route('/backups', methods=['GET'])
def list_backups():
    logs = BackupLog.query.order_by(BackupLog.created_at.desc()).all()
    return jsonify([{'id': l.id, 'filename': l.filename, 'created_at': l.created_at.isoformat(), 'size_bytes': l.size_bytes} for l in logs])
@api_bp.route('/backups', methods=['POST'])
def trigger_backup():
    from ..backup_service import run_backup
    filename = run_backup()
    return jsonify({'status': 'started', 'filename': filename}), 202
