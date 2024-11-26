from typing import Dict
from pilot_api.model.dynamic_thompson_sampling import DynamicThompsonSampling


## TODO: Add methods to save and load model store
class ModelManager:
    def __init__(self):
        self.model_store: Dict[str, DynamicThompsonSampling] = {}

    def add_model(self, project_id: str, model: DynamicThompsonSampling):
        self.model_store[project_id] = model

    def get_model(self, project_id: str):
        if project_id in self.model_store:
            return self.model_store[project_id]
        return None
