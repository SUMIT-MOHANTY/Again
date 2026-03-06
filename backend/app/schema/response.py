from pydantic import BaseModel
class DummyResponse(BaseModel):
    success: bool
    data: dict
