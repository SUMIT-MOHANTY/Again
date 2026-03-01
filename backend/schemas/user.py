from pydantic import BaseModel, EmailStr, field_validator
from .base import BaseSchema

class UserCreateSchema(BaseSchema):
    email: EmailStr
    password: str
    name: str

    @field_validator("password")
    def validate_password(cls, v):
        if len(v) < 6:
            raise ValueError("Password must be at least 6 characters")
        return v

    @field_validator("name")
    def validate_name(cls, v):
        if not v or len(v.strip()) < 2:
            raise ValueError("Name must be at least 2 characters")
        return v.strip()

class UserUpdateSchema(BaseSchema):
    email: EmailStr | None = None
    password: str | None = None
    name: str | None = None

class UserResponse(BaseSchema):
    id: int
    email: str
    name: str
    created_at: str
