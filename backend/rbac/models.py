from sqlalchemy import Column, Integer, String, Enum, Table, ForeignKey
from sqlalchemy.orm import relationship
from backend.database import Base

# Role enum - extended with all fine‑grained values
role_enum = Enum('Admin','Librarian','Member','Guest', name='role_enum')

class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    name = Column(role_enum, unique=True, nullable=False)
    # back‑ref to permissions via association table
    permissions = relationship('Permission', secondary='role_permission', back_populates='roles')

class Permission(Base):
    __tablename__ = 'permissions'
    id = Column(Integer, primary_key=True)
    module = Column(String, nullable=False)  # books|members|transactions|reports
    action = Column(String, nullable=False)  # create|read|update|delete|export
    description = Column(String)
    roles = relationship('Role', secondary='role_permission', back_populates='permissions')

# Association table linking roles ↔ permissions
role_permission = Table(
    'role_permission', Base.metadata,
    Column('role_id', Integer, ForeignKey('roles.id'), primary_key=True),
    Column('permission_id', Integer, ForeignKey('permissions.id'), primary_key=True)
)
