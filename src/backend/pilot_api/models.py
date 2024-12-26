from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from pilot_api.utils import ElementStatus, ProjectStatus


class Element(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    creation_time: datetime
    last_updated_time: datetime
    status: ElementStatus
    success_rate: float
    impression: int
    success_count: int


class ElementCreateRequest(BaseModel):
    name: str
    description: Optional[str] = None
    status: Optional[str] = ElementStatus.ACTIVE
    project_id: Optional[str] = None


class ElementUpdateRequest(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None


class Project(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    creation_time: datetime
    last_updated_time: datetime
    elements: List[ElementCreateRequest] = []
    model_id: str
    status: str


class ProjectCreateRequest(BaseModel):
    name: str
    description: Optional[str] = None
    elements: List[ElementCreateRequest] = []
    status: Optional[str] = ProjectStatus.ACTIVE


class ProjectUpdateRequest(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None


class RecordActionRequest(BaseModel):
    element_id: str
    success: bool
