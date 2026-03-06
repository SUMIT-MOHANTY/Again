from pydantic import BaseModel
from typing import List, Optional

class PortfolioItem(BaseModel):
    id: int
    title: str
    description: str
    category: str
    technologies: List[str]
    image_url: Optional[str] = None
    project_url: Optional[str] = None

class PortfolioResponse(BaseModel):
    items: List[PortfolioItem]
    total: int
