from sqlalchemy.orm import Session
from .models import Role, Permission, role_permission
from .schemas import RoleCreate, PermissionCreate

def get_role_by_name(db: Session, name: str):
    return db.query(Role).filter(Role.name == name).first()

def create_role(db: Session, payload: RoleCreate):
    role = Role(name=payload.name)
    db.add(role)
    db.commit()
    db.refresh(role)
    return role

def get_all_permissions(db: Session):
    return db.query(Permission).all()

def create_permission(db: Session, payload: PermissionCreate):
    perm = Permission(**payload.dict())
    db.add(perm)
    db.commit()
    db.refresh(perm)
    return perm

def set_role_permissions(db: Session, role_name: str, perms: List[PermissionCreate]):
    role = get_role_by_name(db, role_name)
    if not role:
        raise ValueError(f'Role {role_name} not found')
    # clear existing links
    role.permissions = []
    for p in perms:
        perm = db.query(Permission).filter_by(module=p.module, action=p.action).first()
        if not perm:
            perm = Permission(**p.dict())
            db.add(perm)
            db.flush()
        role.permissions.append(perm)
    db.commit()
