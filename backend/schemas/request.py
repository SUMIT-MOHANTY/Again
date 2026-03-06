from pydantic import BaseModel
from typing import Optional

class FlagUpdateRequest(BaseModel):
    enabled: bool
    description: Optional[str] = None
