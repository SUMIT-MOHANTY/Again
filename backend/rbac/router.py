from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import schemas, crud, service
from backend.database import SessionLocal

router = APIRouter(prefix='/rbac', tags=['RBAC'])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/roles', response_model=List[schemas.RoleCreate])
def list_roles(db: Session = Depends(get_db)):
    return db.query(crud.Role).all()

@router.post('/roles', response_model=schemas.RoleCreate, status_code=status.HTTP_201_CREATED)
def create_role(payload: schemas.RoleCreate, db: Session = Depends(get_db)):
    if crud.get_role_by_name(db, payload.name):
        raise HTTPException(status_code=400, detail='Role already exists')
    return crud.create_role(db, payload)

@router.get('/permissions', response_model=List[schemas.PermissionCreate])
def list_permissions(db: Session = Depends(get_db)):
    return crud.get_all_permissions(db)

@router.post('/role-permissions', status_code=status.HTTP_200_OK)
def replace_role_permissions(map_: schemas.RolePermissionMap, db: Session = Depends(get_db)):
    try:
        service.RBACService(db).assign_permissions(map_.role_name, [p.dict() for p in map_.permissions])
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return {'detail': 'Permissions updated'}
