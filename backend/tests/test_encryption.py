import pytest
from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_document_encryption():
    payload = {'title': 'Secret', 'content': 'TopSecret', 'metadata': 'Meta'}
    resp = client.post('/api/v1/documents/', json=payload)
    assert resp.status_code == 201
    doc_id = resp.json()['id']
    from backend.app.db.session import get_db
    with get_db() as db:
        raw = db.execute('SELECT content FROM documents WHERE id = :id', {'id': doc_id}).fetchone()[0]
        assert raw != payload['content']
