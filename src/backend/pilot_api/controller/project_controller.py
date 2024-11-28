from pilot_api.database.project_database import ProjectDbClient
from pilot_api.database.element_database import ElementDbClient
from pilot_api.models import ProjectCreateRequest
from pilot_api.utils import (
    is_string_empty,
    generate_uuid,
    is_valid_uuid,
    get_current_time,
)
from fastapi import HTTPException
from pilot_api.model.model_manager import ModelManager
from pilot_api.model.dynamic_thompson_sampling import DynamicThompsonSampling
from pilot_api.element import Element


class ProjectController:
    def __init__(
        self,
        project_db_client: ProjectDbClient,
        element_db_client: ElementDbClient,
        model_manager: ModelManager,
    ):
        self.project_db_client = project_db_client
        self.element_db_client = element_db_client
        self.model_manager = model_manager

    async def create_project(self, project_create_request: ProjectCreateRequest):
        if is_string_empty(project_create_request.name):
            raise HTTPException(status_code=400, detail="Project name is required")

        project_id = generate_uuid()
        model_id = generate_uuid()

        self.model_manager.add_model(project_id, DynamicThompsonSampling([]))
        data = {
            "id": project_id,
            "name": project_create_request.name,
            "description": project_create_request.description,
            "last_updated_time": get_current_time(),
            "elements": [],  ## TODO: Add support for creating elements
            "model_id": model_id,
        }
        self.project_db_client.insert_data(data)
        return {"id": project_id}

    async def get_project(self, project_id: str):
        if is_string_empty(project_id) or not is_valid_uuid(project_id):
            raise HTTPException(status_code=400, detail="Invalid project id")

        project_data = self.project_db_client.fetch_data({"id": project_id})
        if project_data is None or len(project_data.data) == 0:
            raise HTTPException(status_code=404, detail="Project not found")
        return project_data.data[0]

    async def get_recommendation(self, project_id: str):
        model = self.model_manager.get_model(project_id)
        if model is None:
            raise HTTPException(status_code=500, detail="Model not found")

        project_data = await self.get_project(project_id)
        if len(project_data.elements) != len(model.elements):
            raise HTTPException(
                status_code=500, detail="Model arms does not match project elements"
            )

        return {"element_id": model.get_recommendation()}

    async def record_action(self, project_id: str, element_id: str, success: bool):
        model = self.model_manager.get_model(project_id)
        if model is None:
            raise HTTPException(status_code=500, detail="Model not found")

        model.update(element_id, success)
        element: Element = model.elements[element_id]
        element.update_success_count(success)
        self.element_db_client.update_data(
            {"id": element_id},
            {
                "impression": element.impression,
                "success_count": element.success_count,
                "last_updated_time": get_current_time(),
                "success_rate": element.get_success_rate(),
            },
        )
        return {"action_recorded": True}
