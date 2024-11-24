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
    success_rate: float
    impression: int
    success_count: int


class Project(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    creation_time: datetime
    last_updated_time: datetime
    elements: List[Element] = []
    model_id: str


class ProjectCreateRequest(BaseModel):
    name: str
    description: Optional[str] = None
    elements: List[Element] = []
