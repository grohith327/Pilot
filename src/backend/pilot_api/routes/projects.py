from fastapi import APIRouter
from pilot_api.models import ProjectCreateRequest
from pilot_api.database.project_database import ProjectDbClient
from pilot_api.database.element_database import ElementDbClient
import os

router = APIRouter(prefix="/projects", tags=["projects"])

URL = os.getenv("SUPABASE_URL")
KEY = os.getenv("SUPABASE_ANON_KEY")
project_db_client = ProjectDbClient.get_instance(URL, KEY)
element_db_client = ElementDbClient.get_instance(URL, KEY)


@router.post("/create")
async def create_project(project_create_request: ProjectCreateRequest):
    pass


@router.get("/{project_id}")
async def get_project(project_id: str):
    pass


@router.put("/{project_id}")
async def update_project(project_id: str):
    pass


@router.post("/{project_id}/elements")
async def add_element_to_project(project_id: str, element_id: str):
    pass
