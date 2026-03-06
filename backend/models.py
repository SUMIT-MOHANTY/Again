from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class BackupLog(db.Model):
    __tablename__ = 'backup_log'
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    size_bytes = db.Column(db.BigInteger)
