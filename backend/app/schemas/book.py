from pydantic import BaseModel, Field

class BookBase(BaseModel):
    title: str = Field(..., max_length=200)
    author: str = Field(..., max_length=100)
    isbn: str = Field(..., max_length=20)
    price: float

class BookCreate(BookBase):
    pass

class BookRead(BookBase):
    id: int
    class Config:
        orm_mode = True
