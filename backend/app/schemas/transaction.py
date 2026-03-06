from pydantic import BaseModel
from datetime import datetime

class TransactionRead(BaseModel):
    id: int
    user_id: int
    book_id: int
    timestamp: datetime
    class Config:
        orm_mode = True
