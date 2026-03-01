import pytest

def test_search_portfolios(client, sample_portfolio):
    response = client.get('/api/search?q=portfolio')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)

def test_search_empty_query(client):
    response = client.get('/api/search?q=')
    assert response.status_code == 400

def test_search_no_results(client):
    response = client.get('/api/search?q=nonexistentterm12345')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 0

def test_search_by_title(client, sample_portfolio):
    response = client.get('/api/search?q=My')
    assert response.status_code == 200
    data = response.get_json()
    assert any(p['title'] == 'My Portfolio' for p in data)

def test_search_by_description(client, sample_portfolio):
    response = client.get('/api/search?q=sample')
    assert response.status_code == 200

def test_search_special_characters(client):
    response = client.get('/api/search?q=!@#$%^&*()')
    assert response.status_code == 200

def test_search_sql_injection_attempt(client):
    response = client.get("/api/search?q=' OR '1'='1")
    assert response.status_code == 200

def test_search_with_portfolio_content(client, auth_headers):
    client.post('/api/portfolios', headers=auth_headers, json={
        'title': 'Python Developer Portfolio',
        'description': 'Expert in Django and Flask',
        'projects': [{'name': 'Web App', 'description': 'Built with Python', 'url': 'https://example.com', 'technologies': ['Python', 'Django']}],
        'skills': [{'name': 'Python', 'level': 5}]
    })
    
    response = client.get('/api/search?q=Python')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) >= 1
