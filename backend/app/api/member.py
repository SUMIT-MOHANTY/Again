from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, status
from sqlalchemy.orm import Session
from ..db.session import SessionLocal
from ..models.member import Member
from ..schemas.member import MemberCreate, MemberUpdate, MemberRead
from ..services.avatar import save_avatar
from ..middleware.rbac import require_permission

router = APIRouter(prefix="/members", tags=["Members"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[MemberRead], dependencies=[require_permission("read:member")])
def list_members(db: Session = Depends(get_db)):
    return db.query(Member).all()

@router.get("/{member_id}", response_model=MemberRead, dependencies=[require_permission("read:member")])
def get_member(member_id: int, db: Session = Depends(get_db)):
    member = db.query(Member).filter(Member.id == member_id).first()
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    return member

@router.post("/", response_model=MemberRead, status_code=status.HTTP_201_CREATED, dependencies=[require_permission("create:member")])
def create_member(payload: MemberCreate, db: Session = Depends(get_db)):
    member = Member(**payload.dict())
    db.add(member)
    db.commit()
    db.refresh(member)
    return member

@router.put("/{member_id}", response_model=MemberRead, dependencies=[require_permission("update:member")])
def update_member(member_id: int, payload: MemberUpdate, db: Session = Depends(get_db)):
    member = db.query(Member).filter(Member.id == member_id).first()
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    for field, value in payload.dict(exclude_unset=True).items():
        setattr(member, field, value)
    db.commit()
    db.refresh(member)
    return member

@router.delete("/{member_id}", status_code=status.HTTP_204_NO_CONTENT, dependencies=[require_permission("delete:member")])
def delete_member(member_id: int, db: Session = Depends(get_db)):
    member = db.query(Member).filter(Member.id == member_id).first()
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    db.delete(member)
    db.commit()
    return None

@router.post("/{member_id}/avatar", dependencies=[require_permission("update:member")])
def upload_avatar(member_id: int, file: UploadFile = File(...), db: Session = Depends(get_db)):
    member = db.query(Member).filter(Member.id == member_id).first()
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    path = save_avatar(member_id, file)
    member.avatar_path = path
    db.commit()
    db.refresh(member)
    return {"avatar_path": path}
