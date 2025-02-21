from typing import Dict
from pilot_api.model.dynamic_thompson_sampling import DynamicThompsonSampling
from pilot_api.storage_client import StorageClient
from pilot_api.database.project_database import ProjectDbClient
import logging

logger = logging.getLogger(__name__)


class ModelManager:
    _instance = None

    def __init__(
        self, storage_client: StorageClient, project_db_client: ProjectDbClient
    ):
        self.storage_client = storage_client
        self.model_store: Dict[str, DynamicThompsonSampling] = {}
        self.project_db_client = project_db_client

    def add_model(self, project_id: str, model: DynamicThompsonSampling):
        self.model_store[project_id] = model

    def get_model(self, project_id: str):
        if project_id in self.model_store:
            return self.model_store[project_id]
        return None

    def load_model(self, project_id: str):
        project_data = self.project_db_client.fetch_data({"id": project_id})
        if project_data is None or len(project_data.data) == 0:
            raise RuntimeError(f"Project with id {project_id} not found")

        try:
            model = DynamicThompsonSampling.load_from_checkpoint(
                project_data.data[0]["model_id"], self.storage_client
            )
            self.add_model(project_id, model)
        except Exception as e:
            ## TODO: Handle error by loading a new model
            raise e

    @classmethod
    def get_instance(
        cls, storage_client: StorageClient, project_db_client: ProjectDbClient
    ):
        if cls._instance is None:
            cls._instance = cls(storage_client, project_db_client)
        return cls._instance
