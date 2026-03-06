from fastapi import APIRouter

router = APIRouter()

# Example endpoint (can be expanded later)
@router.get("/health")
def health_check() -> dict:
    return {"status": "ok"}
