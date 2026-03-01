import pytest
import json
from unittest.mock import Mock, patch
from app import create_app
from config import Config


class TestConfig(Config):
    TESTING = True
    DEBUG = True


@pytest.fixture
def client():
    app = create_app(TestConfig)
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_contact_success(client):
    payload = {
        'name': 'John Doe',
        'email': 'john@example.com',
        'subject': 'Test Subject',
        'message': 'Test message content'
    }
    response = client.post('/api/contact',
                          data=json.dumps(payload),
                          content_type='application/json')
    assert response.status_code == 201
    data = json.loads(response.data)
    assert 'message' in data


def test_contact_missing_field(client):
    payload = {
        'name': 'John Doe',
        'email': 'john@example.com'
    }
    response = client.post('/api/contact',
                          data=json.dumps(payload),
                          content_type='application/json')
    assert response.status_code == 400


def test_contact_invalid_email(client):
    payload = {
        'name': 'John Doe',
        'email': 'invalid-email',
        'subject': 'Test',
        'message': 'Test message'
    }
    response = client.post('/api/contact',
                          data=json.dumps(payload),
                          content_type='application/json')
    assert response.status_code == 400


@patch('app.services.email_service.EmailService.send_contact_notification')
def test_email_failure_still_returns_200(mock_notify, client):
    mock_notify.side_effect = Exception("SMTP Error")
    payload = {
        'name': 'John Doe',
        'email': 'john@example.com',
        'subject': 'Test',
        'message': 'Test message'
    }
    response = client.post('/api/contact',
                          data=json.dumps(payload),
                          content_type='application/json')
    assert response.status_code == 500


def test_contact_empty_payload(client):
    response = client.post('/api/contact',
                          data=json.dumps({}),
                          content_type='application/json')
    assert response.status_code == 400
