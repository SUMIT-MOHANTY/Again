from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.db.session import get_db
from backend.app.models import Document
from pydantic import BaseModel

router = APIRouter()

class DocumentCreate(BaseModel):
    title: str
    content: str
    metadata: str | None = None

@router.post('/api/v1/documents/', response_model=dict, status_code=201)
def create_document(payload: DocumentCreate, db: Session = Depends(get_db)):
    doc = Document(title=payload.title, content=payload.content, metadata=payload.metadata)
    db.add(doc)
    db.commit()
    db.refresh(doc)
    return {'id': doc.id, 'title': doc.title}
