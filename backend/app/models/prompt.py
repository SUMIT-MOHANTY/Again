from sqlalchemy import Column, Integer, String, ForeignKey
from ..db import Base

class Prompt(Base):
    __tablename__ = 'prompts'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    content = Column(String)
