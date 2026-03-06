import pytest
from app import create_app, db
from app.models import User, Role, Permission

@pytest.fixture(scope='module')
def test_app():
    app = create_app()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['TESTING'] = True
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

def test_role_permission_relationship(test_app):
    r = Role(name='admin')
    p = Permission(action='create', resource='role')
    r.permissions.append(p)
    db.session.add_all([r, p])
    db.session.commit()
    assert r.permissions[0].action == 'create'
