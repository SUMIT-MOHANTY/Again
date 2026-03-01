from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

portfolio_tech = db.Table('portfolio_tech',
    db.Column('portfolio_id', db.Integer, db.ForeignKey('portfolios.id')),
    db.Column('technology_id', db.Integer, db.ForeignKey('technologies.id'))
)

class Portfolio(db.Model):
    __tablename__ = 'portfolios'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    image_url = db.Column(db.String(500))
    project_url = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    category = db.relationship('Category', backref='portfolios')
    technologies = db.relationship('Technology', secondary=portfolio_tech, backref='portfolios')

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

class Technology(db.Model):
    __tablename__ = 'technologies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
