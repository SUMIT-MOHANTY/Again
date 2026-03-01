import pytest
import json

def test_create_portfolio(client, auth_headers):
    response = client.post('/api/portfolios', headers=auth_headers, json={
        'title': 'My Portfolio',
        'description': 'Portfolio description',
        'projects': [
            {'name': 'Project 1', 'description': 'First project', 'url': 'https://example.com', 'technologies': ['Python']}
        ],
        'skills': [
            {'name': 'Python', 'level': 5}
        ]
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data['title'] == 'My Portfolio'
    assert len(data['projects']) == 1
    assert len(data['skills']) == 1

def test_create_portfolio_unauthorized(client):
    response = client.post('/api/portfolios', json={
        'title': 'My Portfolio',
        'description': 'Test'
    })
    assert response.status_code == 401

def test_list_portfolios(client, sample_portfolio):
    response = client.get('/api/portfolios')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)

def test_get_portfolio_by_id(client, sample_portfolio):
    response = client.get(f'/api/portfolios/{sample_portfolio.id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['title'] == sample_portfolio.title

def test_get_portfolio_not_found(client):
    response = client.get('/api/portfolios/99999')
    assert response.status_code == 404

def test_update_portfolio(client, auth_headers, sample_portfolio):
    response = client.put(f'/api/portfolios/{sample_portfolio.id}', headers=auth_headers, json={
        'title': 'Updated Title',
        'description': 'Updated description'
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data['title'] == 'Updated Title'

def test_update_portfolio_unauthorized(client, sample_portfolio):
    response = client.put(f'/api/portfolios/{sample_portfolio.id}', json={
        'title': 'Updated Title'
    })
    assert response.status_code == 401

def test_update_portfolio_other_user(client, auth_headers, app, db_session):
    from app.models import User, Portfolio
    other_user = User(username='other', email='other@example.com')
    other_user.set_password('pass123')
    db_session.add(other_user)
    db_session.commit()
    
    other_portfolio = Portfolio(user_id=other_user.id, title='Other', description='Other portfolio')
    db_session.add(other_portfolio)
    db_session.commit()
    
    response = client.put(f'/api/portfolios/{other_portfolio.id}', headers=auth_headers, json={
        'title': 'Hacked Title'
    })
    assert response.status_code == 403

def test_delete_portfolio(client, auth_headers, sample_portfolio):
    response = client.delete(f'/api/portfolios/{sample_portfolio.id}', headers=auth_headers)
    assert response.status_code == 200
    
    get_response = client.get(f'/api/portfolios/{sample_portfolio.id}')
    assert get_response.status_code == 404

def test_delete_portfolio_unauthorized(client, sample_portfolio):
    response = client.delete(f'/api/portfolios/{sample_portfolio.id}')
    assert response.status_code == 401

def test_portfolio_with_projects_and_skills(client, auth_headers):
    response = client.post('/api/portfolios', headers=auth_headers, json={
        'title': 'Full Portfolio',
        'description': 'With projects and skills',
        'projects': [
            {'name': 'Project 1', 'description': 'Desc', 'url': 'https://proj1.com', 'technologies': ['React', 'Node']},
            {'name': 'Project 2', 'description': 'Desc 2', 'url': 'https://proj2.com', 'technologies': ['Python']}
        ],
        'skills': [
            {'name': 'JavaScript', 'level': 4},
            {'name': 'Python', 'level': 5}
        ]
    })
    assert response.status_code == 201
    data = response.get_json()
    assert len(data['projects']) == 2
    assert len(data['skills']) == 2
