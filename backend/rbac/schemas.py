from pydantic import BaseModel
from typing import List, Literal

class RoleCreate(BaseModel):
    name: Literal['Admin', 'Librarian', 'Member', 'Guest']

class PermissionCreate(BaseModel):
    module: Literal['books', 'members', 'transactions', 'reports']
    action: Literal['create', 'read', 'update', 'delete', 'export']
    description: str

class RolePermissionMap(BaseModel):
    role_name: str
    permissions: List[PermissionCreate]
