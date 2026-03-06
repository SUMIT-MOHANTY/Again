from pydantic import BaseModel
from typing import List, Optional

class FlagResponse(BaseModel):
    name: str
    enabled: bool
    description: Optional[str] = None

class FlagListResponse(BaseModel):
    flags: List[FlagResponse]
