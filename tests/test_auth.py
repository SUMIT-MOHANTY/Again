import pytest
import json

def test_register_success(client):
    response = client.post('/api/auth/register', json={
        'email': 'newuser@example.com',
        'password': 'securepass123',
        'full_name': 'New User'
    })
    assert response.status_code == 201
    data = response.get_json()
    assert 'user_id' in data
    assert data['email'] == 'newuser@example.com'

def test_register_duplicate_email(client, test_user):
    response = client.post('/api/auth/register', json={
        'email': 'test@example.com',
        'password': 'password123',
        'full_name': 'Duplicate'
    })
    assert response.status_code == 400
    assert 'error' in response.get_json()

def test_register_invalid_email(client):
    response = client.post('/api/auth/register', json={
        'email': 'invalid-email',
        'password': 'password123',
        'full_name': 'Test User'
    })
    assert response.status_code == 400

def test_register_short_password(client):
    response = client.post('/api/auth/register', json={
        'email': 'user@example.com',
        'password': 'short',
        'full_name': 'Test User'
    })
    assert response.status_code == 400

def test_login_success(client, test_user):
    response = client.post('/api/auth/login', json={
        'email': 'test@example.com',
        'password': 'password123'
    })
    assert response.status_code == 200
    data = response.get_json()
    assert 'access_token' in data
    assert 'user' in data

def test_login_invalid_password(client, test_user):
    response = client.post('/api/auth/login', json={
        'email': 'test@example.com',
        'password': 'wrongpassword'
    })
    assert response.status_code == 401

def test_login_nonexistent_user(client):
    response = client.post('/api/auth/login', json={
        'email': 'nonexistent@example.com',
        'password': 'password123'
    })
    assert response.status_code == 401

def test_get_current_user(client, auth_headers):
    response = client.get('/api/auth/me', headers=auth_headers)
    assert response.status_code == 200
    data = response.get_json()
    assert 'email' in data

def test_get_current_user_unauthorized(client):
    response = client.get('/api/auth/me')
    assert response.status_code == 401

def test_logout(client, auth_headers):
    response = client.post('/api/auth/logout', headers=auth_headers)
    assert response.status_code in [200, 401]
