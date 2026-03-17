from flask import Blueprint, jsonify
import psycopg2

health_bp = Blueprint('health', __name__)

@health_bp.route('/health', methods=['GET'])
def health_check():
    try:
        # Add basic health check
        from backend.db import db
        conn = db.get_connection()
        cur = conn.cursor()
        cur.execute("SELECT 1")
        cur.fetchone()
        cur.close()
        db.return_connection(conn)
        return jsonify({'status': 'healthy'}), 200
    except Exception as e:
        return jsonify({'status': 'unhealthy', 'error': str(e)}), 503

@health_bp.route('/ready', methods=['GET'])
def readiness_check():
    return jsonify({'status': 'ready'}), 200
