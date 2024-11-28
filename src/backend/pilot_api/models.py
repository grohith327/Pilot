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


class ElementCreateRequest(BaseModel):
    name: str
    description: Optional[str] = None
    activate: Optional[bool] = True
    project_id: Optional[str] = None


class Project(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    creation_time: datetime
    last_updated_time: datetime
    elements: List[ElementCreateRequest] = []
    model_id: str


class ProjectCreateRequest(BaseModel):
    name: str
    description: Optional[str] = None
    elements: List[ElementCreateRequest] = []


class RecordActionRequest(BaseModel):
    element_id: str
    success: bool
