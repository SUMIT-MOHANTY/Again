from sqlalchemy import Column, Integer, ForeignKey, DateTime, func
from ..database.base import Base

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
