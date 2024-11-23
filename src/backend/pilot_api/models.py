from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class Element(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    creation_time: datetime
    last_updated_time: datetime
    is_active: bool


class Project(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    creation_time: datetime
    last_updated_time: datetime
    elements: List[Element]
