from pilot_api.database.element_database import ElementDbClient
from pilot_api.database.project_database import ProjectDbClient
from pilot_api.models import ElementCreateRequest, ElementUpdateRequest
from pilot_api.utils import (
    is_string_empty,
    is_valid_uuid,
    generate_uuid,
    get_current_time,
)
from fastapi import HTTPException
import logging
from pilot_api.model.model_manager import ModelManager

logger = logging.getLogger(__name__)


class ElementController:
    def __init__(
        self,
        element_db_client: ElementDbClient,
        project_db_client: ProjectDbClient,
        model_manager: ModelManager,
    ):
        self.element_db_client = element_db_client
        self.project_db_client = project_db_client
        self.model_manager = model_manager

    async def create_element(self, element_create_request: ElementCreateRequest):
        if is_string_empty(element_create_request.name):
            raise HTTPException(status_code=400, detail="Element name is required")

        if is_string_empty(element_create_request.project_id) or not is_valid_uuid(
            element_create_request.project_id
        ):
            raise HTTPException(status_code=400, detail="Invalid project id")

        project_data = self.project_db_client.fetch_data(
            {"id": element_create_request.project_id}
        )
        if project_data is None or len(project_data.data) == 0:
            raise HTTPException(status_code=400, detail="Project not found")

        current_time = get_current_time()
        data = {
            "id": generate_uuid(),
            "name": element_create_request.name,
            "description": element_create_request.description,
            "status": element_create_request.status,
            "project_id": element_create_request.project_id,
            "last_updated_time": current_time,
            "creation_time": current_time,
            "impression": 0,
            "success_count": 0,
            "success_rate": 0,
        }
        self.element_db_client.insert_data(data)
        self.project_db_client.update_data(
            {"id": element_create_request.project_id},
            {
                "last_updated_time": current_time,
                "elements": project_data.data[0]["elements"] + [data["id"]],
            },
        )
        logger.info(f"Created element with id {data['id']}")
        return {"data": data}

    async def get_element(self, element_id: str):
        if is_string_empty(element_id) or not is_valid_uuid(element_id):
            raise HTTPException(status_code=400, detail="Invalid element id")

        element_data = self.element_db_client.fetch_data({"id": element_id})
        if element_data is None or len(element_data.data) == 0:
            raise HTTPException(status_code=404, detail="Element not found")

        logger.info(f"Fetched element with id {element_id}")
        return element_data.data[0]

    async def update_element(
        self, element_id: str, element_update_request: ElementUpdateRequest
    ):
        if is_string_empty(element_id) or not is_valid_uuid(element_id):
            raise HTTPException(status_code=400, detail="Invalid element id")

        element_data = self.element_db_client.fetch_data({"id": element_id})
        if element_data is None or len(element_data.data) == 0:
            raise HTTPException(status_code=404, detail="Element not found")

        model = self.model_manager.get_model(element_data.data[0]["project_id"])
        if model is None:
            raise HTTPException(status_code=500, detail="Model not found")

        if element_update_request.status is not None:
            model.update_element_status(element_id, element_update_request.status)

        current_time = get_current_time()
        data = {}
        if not is_string_empty(element_update_request.name):
            data["name"] = element_update_request.name
        if not is_string_empty(element_update_request.description):
            data["description"] = element_update_request.description
        if element_update_request.status is not None:
            data["status"] = element_update_request.status

        if len(data) == 0:
            raise HTTPException(status_code=400, detail="No fields to update")

        data["last_updated_time"] = current_time
        updated_data = self.element_db_client.update_data({"id": element_id}, data)
        logger.info(f"Updated element with id {element_id}")
        return updated_data.data[0]
