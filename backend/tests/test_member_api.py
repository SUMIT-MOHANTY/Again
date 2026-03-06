import pytest
from httpx import AsyncClient
from fastapi import FastAPI
from pathlib import Path
from ..app.main import app as fastapi_app
from ..app.config import UPLOAD_DIR

@pytest.fixture
def anyio_backend():
    return 'asyncio'

@pytest.fixture
async def client():
    async with AsyncClient(app=fastapi_app, base_url="http://test") as ac:
        yield ac

@pytest.mark.anyio
async def test_member_crud_and_avatar(client: AsyncClient):
    # Create a member
    payload = {"name": "John Doe", "email": "john@example.com"}
    r = await client.post("/members/", json=payload)
    assert r.status_code == 201
    member = r.json()
    member_id = member["id"]

    # Upload avatar (stub file)
    avatar_content = b"fake image data"
    files = {"avatar": ("avatar.png", avatar_content, "image/png")}
    r = await client.post(f"/members/{member_id}/avatar", files=files)
    assert r.status_code == 200
    assert "avatar_path" in r.json()
    # Verify file exists
    avatar_path = Path(r.json()["avatar_path"])
    assert avatar_path.exists()

    # Update status
    r = await client.put(f"/members/{member_id}", json={"status": "inactive"})
    assert r.status_code == 200
    assert r.json()["status"] == "inactive"

    # Cleanup uploaded file
    if avatar_path.exists():
        avatar_path.unlink()
