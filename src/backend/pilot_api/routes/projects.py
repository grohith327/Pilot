from fastapi import APIRouter
from pilot_api.models import ProjectCreateRequest
from pilot_api.database.project_database import ProjectDbClient
from pilot_api.database.element_database import ElementDbClient
from pilot_api.utils import SUPABASE_URL, SUPABASE_KEY
from pilot_api.controller.project_controller import ProjectController

router = APIRouter(prefix="/projects", tags=["projects"])

project_db_client = ProjectDbClient.get_instance(SUPABASE_URL, SUPABASE_KEY)
element_db_client = ElementDbClient.get_instance(SUPABASE_URL, SUPABASE_KEY)
project_controller = ProjectController(project_db_client, element_db_client)


@router.post("/create")
async def create_project(project_create_request: ProjectCreateRequest):
    return await project_controller.create_project(project_create_request)


@router.get("/{project_id}")
async def get_project(project_id: str):
    return await project_controller.get_project(project_id)


@router.put("/{project_id}")
async def update_project(project_id: str):
    pass


@router.post("/{project_id}/elements")
async def add_element_to_project(project_id: str, element_id: str):
    pass
