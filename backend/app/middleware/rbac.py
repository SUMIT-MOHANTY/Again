from fastapi import Depends, HTTPException, Request
from typing import Callable

def require_permission(permission: str) -> Callable:
    def dependency(request: Request):
        user = getattr(request.state, "user", None)
        if not user or permission not in user.get("permissions", []):
            raise HTTPException(status_code=403, detail="Forbidden")
        return True
    return Depends(dependency)
