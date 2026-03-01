import pytest
import json

def test_404_not_found(client):
    response = client.get('/api/nonexistent')
    assert response.status_code == 404

def test_400_bad_json(client):
    response = client.post('/api/auth/register', data='not json')
    assert response.status_code == 400

def test_400_missing_required_field(client):
    response = client.post('/api/auth/register', json={
        'email': 'test@example.com'
    })
    assert response.status_code == 400

def test_401_unauthorized_access(client):
    response = client.get('/api/auth/me')
    assert response.status_code == 401

def test_403_forbidden(client, auth_headers, app, db_session):
    from app.models import User, Portfolio
    other_user = User(username='other', email='other@test.com')
    other_user.set_password('pass')
    db_session.add(other_user)
    db_session.commit()
    
    other_portfolio = Portfolio(user_id=other_user.id, title='Private', description='Private')
    db_session.add(other_portfolio)
    db_session.commit()
    
    response = client.delete(f'/api/portfolios/{other_portfolio.id}', headers=auth_headers)
    assert response.status_code == 403

def test_422_invalid_field_type(client, auth_headers):
    response = client.post('/api/portfolios', headers=auth_headers, json={
        'title': 12345,
        'description': 'Test'
    })
    assert response.status_code in [400, 422]

def test_empty_body(client):
    response = client.post('/api/auth/register', json={})
    assert response.status_code == 400

def test_null_values(client):
    response = client.post('/api/auth/register', json={
        'email': None,
        'password': None,
        'full_name': None
    })
    assert response.status_code == 400

def test_large_payload(client, auth_headers):
    large_title = 'A' * 10000
    response = client.post('/api/portfolios', headers=auth_headers, json={
        'title': large_title,
        'description': 'Test'
    })
    assert response.status_code in [200, 400, 413]

def test_invalid_portfolio_id(client, auth_headers):
    response = client.get('/api/portfolios/invalid_id')
    assert response.status_code in [404, 400]

def test_portfolio_id_zero(client):
    response = client.get('/api/portfolios/0')
    assert response.status_code == 404

def test_portfolio_id_negative(client):
    response = client.get('/api/portfolios/-1')
    assert response.status_code == 404
