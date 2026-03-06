from sqlalchemy import Column, Integer, ForeignKey, Index
from . import Base
class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    member_id = Column(Integer, ForeignKey('members.id'))
    checkout_date = Column(String)
    return_date = Column(String, nullable=True)
    __table_args__ = (Index('ix_tx_member_book', 'member_id', 'book_id'),)
