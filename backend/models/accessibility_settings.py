from . import db
from uuid import uuid4
from datetime import datetime

class AccessibilitySettings(db.Model):
    __tablename__ = 'accessibility_settings'
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    page_path = db.Column(db.String(255), unique=True, nullable=False)
    high_contrast_enabled = db.Column(db.Boolean, default=False)
    reduced_motion_enabled = db.Column(db.Boolean, default=False)
    font_size_multiplier = db.Column(db.Float, default=1.0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
