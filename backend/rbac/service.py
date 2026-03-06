from typing import Dict, List
from sqlalchemy.orm import Session
from .models import Role, Permission

class RBACService:
    def __init__(self, db: Session):
        self.db = db

    def get_permission_matrix(self) -> Dict[str, Dict[str, List[str]]]:
        matrix: Dict[str, Dict[str, List[str]]] = {}
        roles = self.db.query(Role).all()
        for role in roles:
            matrix[role.name] = {}
            for perm in role.permissions:
                matrix[role.name].setdefault(perm.module, []).append(perm.action)
        return matrix

    def assign_permissions(self, role_name: str, perms: List[Dict]):
        from .crud import set_role_permissions
        # Convert plain dicts to PermissionCreate‑like objects
        class Dummy:
            def __init__(self, d): self.__dict__ = d
        objs = [Dummy(p) for p in perms]
        set_role_permissions(self.db, role_name, objs)
