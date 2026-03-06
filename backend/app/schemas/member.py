from typing import Optional
from pydantic import BaseModel

class MemberBase(BaseModel):
    avatar_path: Optional[str] = None
    status: Optional[str] = "active"
    role_id: Optional[int] = None

class MemberCreate(MemberBase):
    name: str
    email: str

class MemberUpdate(MemberBase):
    name: Optional[str] = None
    email: Optional[str] = None

class MemberRead(MemberBase):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True
