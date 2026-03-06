from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..db import get_db
from ..schemas.book import BookCreate, BookRead, BookUpdate
from ..services.book_service import (
    get_books, get_book, create_book, update_book, delete_book
)

router = APIRouter()

@router.get("/", response_model=list[BookRead])
def list_books(skip: int = 0, limit: int = 10, q: str | None = None, db: Session = Depends(get_db)):
    return get_books(db, skip=skip, limit=limit, search=q)

@router.get("/{book_id}", response_model=BookRead)
def read_book(book_id: int, db: Session = Depends(get_db)):
    book = get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return book

@router.post("/", response_model=BookRead, status_code=status.HTTP_201_CREATED)
def create_new_book(payload: BookCreate, db: Session = Depends(get_db)):
    return create_book(db, payload)

@router.put("/{book_id}", response_model=BookRead)
def update_existing_book(book_id: int, payload: BookUpdate, db: Session = Depends(get_db)):
    book = update_book(db, book_id, payload)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return book

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_book(book_id: int, db: Session = Depends(get_db)):
    success = delete_book(db, book_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return None
