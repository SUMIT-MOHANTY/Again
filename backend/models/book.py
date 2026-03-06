from sqlalchemy import Column, Integer, String, Index
from . import Base
class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    isbn = Column(String, unique=True, nullable=False)
    published_year = Column(Integer)
    __table_args__ = (
        Index('ix_book_isbn', 'isbn'),
        Index('ix_book_title', 'title'),
    )
