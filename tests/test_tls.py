import pytest, requests

def test_http_redirect():
    resp = requests.get('http://localhost:8080/health', allow_redirects=False)
    assert resp.status_code in (301, 302)
    assert resp.headers.get('Location', '').startswith('https://')

def test_https_success():
    resp = requests.get('https://localhost:8443/health', verify=False)
    assert resp.status_code == 200
    json = resp.json()
    assert json.get('data', {}).get('alive') is True
