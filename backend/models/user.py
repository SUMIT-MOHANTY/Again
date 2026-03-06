from sqlalchemy import Column, Integer, String, LargeBinary
from .base import Base  # assumed existing Base class

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    # Encrypted SSN stored as BYTEA; plain SSN column removed.
    encrypted_ssn = Column(LargeBinary, nullable=True, default=None)
