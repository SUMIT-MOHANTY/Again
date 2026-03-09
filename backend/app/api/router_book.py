from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from .. import schemas, models, dependencies

router = APIRouter(prefix="/books", tags=["books"])

@router.post("/", response_model=schemas.BookRead)
async def create_book(book: schemas.BookCreate, db: AsyncSession = Depends(dependencies.get_db)):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    await db.commit()
    await db.refresh(db_book)
    return db_book
