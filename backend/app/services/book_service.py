from sqlalchemy.orm import Session
from ..models.book import Book
from ..schemas.book import BookCreate, BookUpdate

def get_books(db: Session, skip: int = 0, limit: int = 10, search: str | None = None):
    query = db.query(Book)
    if search:
        query = query.filter(Book.title.ilike(f"%{search}%"))
    return query.offset(skip).limit(limit).all()

def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def create_book(db: Session, payload: BookCreate):
    db_book = Book(**payload.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def update_book(db: Session, book_id: int, payload: BookUpdate):
    db_book = get_book(db, book_id)
    if not db_book:
        return None
    for field, value in payload.dict(exclude_unset=True).items():
        setattr(db_book, field, value)
    db.commit()
    db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int) -> bool:
    db_book = get_book(db, book_id)
    if not db_book:
        return False
    db.delete(db_book)
    db.commit()
    return True
