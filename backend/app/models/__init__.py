from ..db import Base
from sqlalchemy import Column, Integer, String, Text

class Prompt(Base):
    __tablename__ = "prompts"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    content = Column(Text, nullable=False)

class Completion(Base):
    __tablename__ = "completions"
    id = Column(Integer, primary_key=True, index=True)
    prompt_id = Column(Integer, index=True)
    result = Column(Text, nullable=False)
