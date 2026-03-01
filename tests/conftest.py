import pytest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))

from app import create_app
from app.models import db, User, Portfolio

@pytest.fixture(scope='session')
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['JWT_SECRET_KEY'] = 'test-secret-key'
    app.config['WTF_CSRF_ENABLED'] = False
    
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture(scope='function')
def client(app):
    return app.test_client()

@pytest.fixture(scope='function')
def db_session(app):
    with app.app_context():
        yield db.session
        db.session.rollback()
        for table in reversed(db.metadata.sorted_tables):
            db.session.execute(table.delete())
        db.session.commit()

@pytest.fixture
def test_user(app, db_session):
    from app.services.auth_service import AuthService
    user = AuthService.register_user('testuser', 'test@example.com', 'password123')
    return user

@pytest.fixture
def auth_token(client, test_user):
    response = client.post('/api/auth/login', json={
        'email': 'test@example.com',
        'password': 'password123'
    })
    return response.json.get('access_token')

@pytest.fixture
def auth_headers(auth_token):
    return {'Authorization': f'Bearer {auth_token}', 'Content-Type': 'application/json'}

@pytest.fixture
def sample_portfolio(app, db_session, test_user):
    portfolio = Portfolio(
        user_id=test_user.id,
        title='My Portfolio',
        description='A sample portfolio'
    )
    db_session.add(portfolio)
    db_session.commit()
    return portfolio
