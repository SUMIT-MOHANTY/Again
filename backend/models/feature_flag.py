from pydantic import BaseModel
from typing import Optional

class FeatureFlag(BaseModel):
    name: str
    enabled: bool
    description: Optional[str] = None
