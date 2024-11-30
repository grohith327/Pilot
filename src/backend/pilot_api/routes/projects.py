from fastapi import APIRouter
from pilot_api.models import (
    ProjectCreateRequest,
    RecordActionRequest,
    ProjectUpdateRequest,
)
from pilot_api.database.project_database import ProjectDbClient
from pilot_api.database.element_database import ElementDbClient
from pilot_api.utils import SUPABASE_URL, SUPABASE_KEY
from pilot_api.controller.project_controller import ProjectController
from pilot_api.model.model_manager import ModelManager
from pilot_api.storage_client import StorageClient

router = APIRouter(prefix="/projects", tags=["projects"])

project_db_client = ProjectDbClient.get_instance(SUPABASE_URL, SUPABASE_KEY)
element_db_client = ElementDbClient.get_instance(SUPABASE_URL, SUPABASE_KEY)
storage_client = StorageClient.get_instance(SUPABASE_URL, SUPABASE_KEY)
model_manager = ModelManager.get_instance(storage_client, project_db_client)
project_controller = ProjectController(
    project_db_client, element_db_client, model_manager
)


@router.post("/create")
async def create_project(project_create_request: ProjectCreateRequest):
    return await project_controller.create_project(project_create_request)


@router.get("/{project_id}")
async def get_project(project_id: str):
    return await project_controller.get_project(project_id)


@router.put("/{project_id}")
async def update_project(project_id: str, project_update_request: ProjectUpdateRequest):
    return await project_controller.update_project(project_id, project_update_request)


@router.get("/{project_id}/recommendation")
async def get_recommedation(project_id: str):
    return await project_controller.get_recommendation(project_id)


@router.post("/{project_id}/record-action")
async def record_action(project_id: str, record_action_request: RecordActionRequest):
    return await project_controller.record_action(
        project_id, record_action_request.element_id, record_action_request.success
    )
