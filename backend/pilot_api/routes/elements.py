from fastapi import APIRouter
from pilot_api.utils import SUPABASE_URL, SUPABASE_KEY
from pilot_api.database.element_database import ElementDbClient
from pilot_api.database.project_database import ProjectDbClient
from pilot_api.models import ElementCreateRequest, ElementUpdateRequest
from pilot_api.controller.element_controller import ElementController
from pilot_api.model.model_manager import ModelManager
from pilot_api.storage_client import StorageClient


router = APIRouter(prefix="/elements", tags=["elements"])

element_db_client = ElementDbClient.get_instance(SUPABASE_URL, SUPABASE_KEY)
project_db_client = ProjectDbClient.get_instance(SUPABASE_URL, SUPABASE_KEY)
storage_client = StorageClient.get_instance(SUPABASE_URL, SUPABASE_KEY)
model_manager = ModelManager.get_instance(storage_client, project_db_client)
element_controller = ElementController(
    element_db_client, project_db_client, model_manager
)


@router.post("/create")
async def create_element(element_create_request: ElementCreateRequest):
    return await element_controller.create_element(element_create_request)


@router.get("/{element_id}")
async def get_element(element_id: str):
    return await element_controller.get_element(element_id)


@router.put("/{element_id}")
async def update_element(element_id: str, element_update_request: ElementUpdateRequest):
    return await element_controller.update_element(element_id, element_update_request)
