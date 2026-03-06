from sqlalchemy import Column, Integer, String, Index
from . import Base
class Member(Base):
    __tablename__ = 'members'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    membership_date = Column(String)
    __table_args__ = (Index('ix_member_email', 'email'),)
