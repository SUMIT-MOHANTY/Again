from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
    username: str = Field(..., max_length=50)
    email: EmailStr

class UserCreate(UserBase):
    password: str = Field(..., min_length=6)

class UserRead(UserBase):
    id: int
    class Config:
        orm_mode = True
