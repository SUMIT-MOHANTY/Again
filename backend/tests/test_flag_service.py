import pytest
from fastapi.testclient import TestClient
from ..app import create_app
from ..services.flag_service import FlagService
from ..models.feature_flag import FeatureFlag

@pytest.fixture
def store():
    return {'feature-a': {'enabled': True, 'description': 'A'}, 'feature-b': {'enabled': False}}

@pytest.fixture
def service(store):
    return FlagService(store)

def test_list_flags(service):
    flags = service.list_flags()
    assert len(flags) == 2
    names = {f.name for f in flags}
    assert names == {'feature-a', 'feature-b'}

def test_get_flag(service):
    f = service.get_flag('feature-a')
    assert f.enabled is True
    assert f.description == 'A'

def test_set_flag_create(service):
    f = service.set_flag('new-flag', True, 'new')
    assert f.name == 'new-flag'
    assert f.enabled is True
    assert f.description == 'new'
    assert service.get_flag('new-flag').enabled is True

def test_set_flag_update(service):
    f = service.set_flag('feature-b', True)
    assert f.enabled is True
    assert service.get_flag('feature-b').enabled is True

def test_api_endpoints():
    app = create_app()
    client = TestClient(app)
    resp = client.get('/api/v1/flags')
    assert resp.status_code == 200
    data = resp.json()
    assert 'flags' in data
    # create new flag via POST
    resp2 = client.post('/api/v1/flags/test-flag', json={'enabled': False})
    assert resp2.status_code == 200
    assert resp2.json()['name'] == 'test-flag'
    # toggle it
    resp3 = client.post('/api/v1/flags/test-flag', json={'enabled': True})
    assert resp3.status_code == 200
    assert resp3.json()['enabled'] is True
