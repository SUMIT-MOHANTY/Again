from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Member(Base):
    __tablename__ = "members"
    id = Column(Integer, primary_key=True, index=True)
    # Existing fields (e.g., name, email) are assumed to be defined elsewhere
    avatar_path = Column(String, nullable=True)
    status = Column(String, default="active")
    role_id = Column(Integer, ForeignKey("roles.id"), nullable=True)
    role = relationship("Role", back_populates="members")
