from fastapi import APIRouter, Depends, HTTPException
from typing import List
from ...services.flag_service import FlagService
from ...schemas.request import FlagUpdateRequest
from ...schemas.response import FlagResponse, FlagListResponse
from ..dependencies import get_flag_store

router = APIRouter()

@router.get('/api/v1/flags', response_model=FlagListResponse)
def list_flags(store: dict = Depends(get_flag_store)):
    service = FlagService(store)
    flags = service.list_flags()
    return FlagListResponse(flags=[FlagResponse(**f.dict()) for f in flags])

@router.post('/api/v1/flags/{name}', response_model=FlagResponse)
def upsert_flag(name: str, req: FlagUpdateRequest, store: dict = Depends(get_flag_store)):
    service = FlagService(store)
    try:
        flag = service.set_flag(name, req.enabled, req.description)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return FlagResponse(**flag.dict())
