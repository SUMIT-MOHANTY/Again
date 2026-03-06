from sqlalchemy import Column, Integer, String, ForeignKey
from ..db import Base

class Completion(Base):
    __tablename__ = 'completions'
    id = Column(Integer, primary_key=True, index=True)
    prompt_id = Column(Integer, ForeignKey('prompts.id'))
    result = Column(String)
