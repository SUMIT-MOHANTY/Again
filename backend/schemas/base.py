from pydantic import BaseModel, validator
from typing import Optional, Any

class BaseSchema(BaseModel):
    class Config:
        extra = "forbid"

    @validator("*_id", pre=True, always=True)
    def convert_id(cls, v):
        if isinstance(v, str) and v.isdigit():
            return int(v)
        return v
