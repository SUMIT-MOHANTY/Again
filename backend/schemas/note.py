from pydantic import BaseModel

class NoteCreate(BaseModel):
    content: str

class NoteRead(BaseModel):
    id: int
    user_id: int
    content: str
