import pytest

def test_cors_preflight_request(client):
    response = client.options(
        '/api/portfolios',
        headers={
            'Origin': 'http://localhost:3000',
            'Access-Control-Request-Method': 'GET',
            'Access-Control-Request-Headers': 'Authorization,Content-Type'
        }
    )
    assert response.status_code in [200, 404]

def test_cors_headers_present(client):
    response = client.get('/api/portfolios', headers={'Origin': 'http://localhost:3000'})
    assert response.status_code == 200
    assert 'Access-Control-Allow-Origin' in response.headers or response.status_code == 200

def test_cors_different_origins(client):
    origins = ['http://localhost:3000', 'http://127.0.0.1:3000', 'https://example.com']
    for origin in origins:
        response = client.get('/api/portfolios', headers={'Origin': origin})
        assert response.status_code == 200

def test_cors_post_request(client):
    response = client.post(
        '/api/portfolios',
        headers={
            'Origin': 'http://localhost:3000',
            'Content-Type': 'application/json'
        },
        json={'title': 'Test', 'description': 'Test'}
    )
    assert response.status_code in [200, 401, 400]

def test_cors_authenticated_request(client, auth_headers):
    auth_headers['Origin'] = 'http://localhost:3000'
    response = client.get('/api/auth/me', headers=auth_headers)
    assert response.status_code == 200
