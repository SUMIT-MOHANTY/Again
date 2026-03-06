from sqlalchemy.orm import Session
from backend.database import SessionLocal
from .service import RBACService
from .schemas import RoleCreate, PermissionCreate

def _default_permissions() -> Dict[str, List[PermissionCreate]]:
    from collections import defaultdict
    perms = defaultdict(list)
    modules = ['books', 'members', 'transactions', 'reports']
    actions = ['create','read','update','delete','export']
    # Admin gets everything
    for m in modules:
        for a in actions:
            perms['Admin'].append(PermissionCreate(module=m, action=a, description=f'Admin {a} {m}'))
    # Librarian - all except delete on reports
    for m in modules:
        for a in actions:
            if not (m == 'reports' and a == 'delete'):
                perms['Librarian'].append(PermissionCreate(module=m, action=a, description=f'Librarian {a} {m}'))
    # Member - read on books & members, create/read on transactions, export on reports
    for a in ['read']:
        perms['Member'].append(PermissionCreate(module='books', action=a, description=''))
        perms['Member'].append(PermissionCreate(module='members', action=a, description=''))
    perms['Member'].append(PermissionCreate(module='transactions', action='create', description=''))
    perms['Member'].append(PermissionCreate(module='transactions', action='read', description=''))
    perms['Member'].append(PermissionCreate(module='reports', action='export', description=''))
    # Guest - only read books
    perms['Guest'].append(PermissionCreate(module='books', action='read', description=''))
    return perms

def run():
    db: Session = SessionLocal()
    svc = RBACService(db)
    # create roles if missing
    for role in ['Admin','Librarian','Member','Guest']:
        if not svc.db.query(svc.db.query(svc.db.query).filter_by(name=role).first()):
            db.add(svc.db.query(svc.db.mapper).class_(name=role))
    db.commit()
    perms = _default_permissions()
    for role, plist in perms.items():
        svc.assign_permissions(role, [p.dict() for p in plist])
    db.close()

if __name__ == '__main__':
    run()
