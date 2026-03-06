from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import get_db
from .. import models, cache

router = APIRouter()

CACHE_PREFIX = "book:"  # simple key prefix

@router.get("/books/{book_id}", response_model=dict)
async def get_book(book_id: int, db: AsyncSession = Depends(get_db)):
    cache_key = f"{CACHE_PREFIX}{book_id}"
    cached = await cache.get(cache_key)
    if cached:
        return cached
    result = await db.get(models.Book, book_id)
    if not result:
        raise HTTPException(status_code=404, detail="Book not found")
    payload = {"id": result.id, "title": result.title, "author": result.author, "description": result.description}
    await cache.set(cache_key, payload)
    return payload
