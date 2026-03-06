import json
from backend.app import create_app

def test_default_version_routes_to_v1():
    app = create_app()
    client = app.test_client()
    resp = client.post('/api/auth/login', json={"username": "test", "password": "secret"})
    assert resp.status_code == 200
    data = resp.get_json()
    assert "access_token" in data

def test_supported_version_access():
    app = create_app()
    client = app.test_client()
    resp = client.get('/api/v1/users')
    assert resp.status_code == 200

def test_unsupported_version_returns_404():
    app = create_app()
    client = app.test_client()
    resp = client.get('/api/v9/users')
    assert resp.status_code == 404
    data = resp.get_json()
    assert data["error"] == "API version not supported"
    assert "v1" in data["supported_versions"]
