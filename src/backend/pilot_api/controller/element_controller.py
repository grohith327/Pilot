from pilot_api.database.element_database import ElementDbClient
from pilot_api.database.project_database import ProjectDbClient
from pilot_api.models import ElementCreateRequest
from pilot_api.utils import (
    is_string_empty,
    is_valid_uuid,
    generate_uuid,
    get_current_time,
)
from fastapi import HTTPException


class ElementController:
    def __init__(
        self, element_db_client: ElementDbClient, project_db_client: ProjectDbClient
    ):
        self.element_db_client = element_db_client
        self.project_db_client = project_db_client

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
        if project_data is None:
            raise HTTPException(status_code=400, detail="Project not found")

        current_time = get_current_time()
        data = {
            "id": generate_uuid(),
            "name": element_create_request.name,
            "description": element_create_request.description,
            "is_active": element_create_request.activate,
            "project_id": element_create_request.project_id,
            "last_updated_time": current_time,
            "creation_time": current_time,
            "impression": 0,
            "success_count": 0,
            "success_rate": 0,
        }
        self.element_db_client.insert_data(data)
        return {"id": data["id"]}

    async def get_element(self, element_id: str):
        if is_string_empty(element_id) or not is_valid_uuid(element_id):
            raise HTTPException(status_code=400, detail="Invalid element id")

        element_data = self.element_db_client.fetch_data({"id": element_id})
        if element_data is None or len(element_data.data) == 0:
            raise HTTPException(status_code=404, detail="Element not found")

        return element_data.data[0]
