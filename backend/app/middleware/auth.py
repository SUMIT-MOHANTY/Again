from fastapi import Request
async def fake_auth_middleware(request: Request, call_next):
    # Stub user with all permissions for testing purposes
    request.state.user = {"id": 1, "permissions": ["read:member", "create:member", "update:member", "delete:member"]}
    response = await call_next(request)
    return response
