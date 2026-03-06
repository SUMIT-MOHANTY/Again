import pytest
from fastapi.testclient import TestClient
from backend.app import app

client = TestClient(app)

@pytest.fixture(scope='module')
def seed_db():
    # assume the seed script has been run in test env
    pass

def test_get_roles(seed_db):
    resp = client.get('/rbac/roles')
    assert resp.status_code == 200
    names = [r['name'] for r in resp.json()]
    for role in ['Admin','Librarian','Member','Guest']:
        assert role in names

def test_create_duplicate_role(seed_db):
    resp = client.post('/rbac/roles', json={'name': 'Admin'})
    assert resp.status_code == 400

def test_assign_role_permissions(seed_db):
    payload = {
        'role_name': 'Guest',
        'permissions': [
            {'module': 'books', 'action': 'read', 'description': 'guest read books'}
        ]
    }
    resp = client.post('/rbac/role-permissions', json=payload)
    assert resp.status_code == 200
    assert resp.json()['detail'] == 'Permissions updated'
