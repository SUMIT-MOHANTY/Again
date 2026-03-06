import pytest
from fastapi.testclient import TestClient
from ..app import create_app
from ..config import settings
from ..dependencies.database import get_db
from ..crud.user import get_user_by_id

client = TestClient(create_app())

@pytest.fixture(scope='function')
def db_session():
    # Simple fixture that yields a DB session; assumes get_db yields a Session.
    from ..dependencies.database import SessionLocal
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_user_ssn_is_encrypted(db_session):
    payload = {"name": "Alice", "email": "alice@example.com", "ssn": "123-45-6789"}
    resp = client.post('/api/v1/users', json=payload)
    assert resp.status_code == 201
    user_id = resp.json()["id"]
    db_user = get_user_by_id(db_session, user_id)
    assert db_user is not None
    assert isinstance(db_user.encrypted_ssn, (bytes, bytearray))
    assert db_user.encrypted_ssn != payload["ssn"].encode()

def test_backup_contains_encrypted_blob(db_session):
    # Simulate a backup dump by reading the raw encrypted column.
    user = db_session.query(User).first()
    assert isinstance(user.encrypted_ssn, (bytes, bytearray))
