from fastapi import APIRouter, HTTPException
from ..service.service import fetch_external_data
api_router = APIRouter()
@api_router.get('/v1/external-data')
async def external_data():
    try:
        data = await fetch_external_data()
        return {'success': True, 'data': data}
    except Exception as e:
        raise HTTPException(status_code=502, detail=str(e))
@api_router.get('/health')
async def health():
    return {'status': 'ok'}
@api_router.get('/ready')
async def ready():
    return {'ready': True}
