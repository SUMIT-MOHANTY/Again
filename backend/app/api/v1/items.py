from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..dependencies import get_db, get_current_active_user
from ...schemas.item import ItemCreate, ItemRead
from ...models.item import Item

router = APIRouter()

@router.post('/', response_model=ItemRead)
def create_item(item_in: ItemCreate, db: Session = Depends(get_db), user=Depends(get_current_active_user)):
    db_item = Item(**item_in.dict(), owner_id=user.id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get('/{item_id}', response_model=ItemRead)
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail='Item not found')
    return item
