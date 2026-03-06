from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .. import schemas, models, dependencies

router = APIRouter(prefix="/transactions", tags=["transactions"])

@router.get("/", response_model=list[schemas.TransactionRead])
async def list_transactions(db: AsyncSession = Depends(dependencies.get_db)):
    result = await db.execute(models.Transaction.__table__.select())
    return result.scalars().all()
