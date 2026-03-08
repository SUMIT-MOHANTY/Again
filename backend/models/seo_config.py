from . import db
from uuid import uuid4
from datetime import datetime

class SEOConfig(db.Model):
    __tablename__ = 'seo_configs'
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    path = db.Column(db.String(255), unique=True, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    meta_description = db.Column(db.Text)
    og_image = db.Column(db.String(500))
    canonical_url = db.Column(db.String(500))
    sitemap_priority = db.Column(db.Float, default=0.5)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
