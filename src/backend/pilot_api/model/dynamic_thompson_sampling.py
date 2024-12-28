from pilot_api.model.base_bandit_algorithm import BanditAlgorithm
from pilot_api.storage_client import StorageClient
from pilot_api.utils import MODEL_CHECKPOINT_BUCKET
from pilot_api.element import Element
import numpy as np
import json
import logging
from supabase import StorageException

logger = logging.getLogger(__name__)


class DynamicThompsonSampling(BanditAlgorithm):
    def __init__(
        self,
        model_id: str,
        elements: list[Element],
        storage_client: StorageClient,
        alpha: float = 1.0,
        beta: float = 1.0,
        save_interval: int = 100,
    ):
        self.alpha = alpha
        self.beta = beta
        self.elements = {}
        self.model_id = model_id
        self.storage_client = storage_client
        self.save_interval = save_interval
        self._model_update_counter = 0

        self.add_elements(elements)

    def add_elements(self, new_elements: list[Element]):
        if len(self.elements) != 0:
            active_elements = [
                element
                for element in self.elements.values()
                if element.status == "Active"
            ]
            if len(active_elements) != 0:
                logger.warning(
                    f"Active elements found. Updating alpha and beta. Current number of active elements: {len(active_elements)}"
                )
                total_impressions = sum(
                    element.impression for element in active_elements
                )
                total_success_count = sum(
                    element.success_count for element in active_elements
                )
                avg_success_rate = (
                    total_success_count / total_impressions
                    if total_impressions > 0
                    else 0.5
                )

                self.alpha = avg_success_rate * 100
                self.beta = (1 - avg_success_rate) * 100

        for new_element in new_elements:
            if new_element.id not in self.elements:
                self.elements[new_element.id] = new_element
            else:
                self.elements[new_element.id].status = "Active"
        logger.warning(f"Added {len(new_elements)} elements to the algorithm")

    def remove_elements(self, elements_to_remove: list[Element]):
        for element_to_remove in elements_to_remove:
            if element_to_remove.id in self.elements:
                self.elements[element_to_remove.id].status = "Inactive"
        logger.warning(f"Removed {len(elements_to_remove)} elements from the algorithm")

    def update_element_status(self, element_id: str, status: str):
        if element_id not in self.elements:
            raise ValueError(f"Element with id {element_id} not found")
        self.elements[element_id].status = status

    def get_recommendation(self) -> str:
        active_elements = {
            k: v for k, v in self.elements.items() if v.status == "Active"
        }
        if not active_elements:
            raise ValueError("No active elements found")

        scores = {}
        for element_id, element in active_elements.items():
            alpha = self.alpha + element.success_count
            beta = self.beta + (element.impression - element.success_count)
            scores[element_id] = np.random.beta(alpha, beta)

        return max(scores.items(), key=lambda x: x[1])[0]

    def update(self, element_id: str, reward: bool):
        if element_id not in self.elements:
            raise ValueError(f"Element with id {element_id} not found")
        self.elements[element_id].update_success_count(reward)
        self._model_update_counter += 1
        if self._model_update_counter % self.save_interval == 0:
            self.save_checkpoint()
            self._model_update_counter = 0

    def save_checkpoint(self):
        state = {
            "elements": {k: v.to_dict() for k, v in self.elements.items()},
            "alpha": self.alpha,
            "beta": self.beta,
            "model_id": self.model_id,
        }
        json_state = json.dumps(state).encode("utf-8")
        save_path = f"{self.model_id}.json"
        self.storage_client.write_file(
            MODEL_CHECKPOINT_BUCKET,
            save_path,
            json_state,
        )
        logger.info(f"Saved model checkpoint to {save_path}")

    @classmethod
    def load_from_checkpoint(
        cls, model_id: str, storage_client: StorageClient
    ) -> "DynamicThompsonSampling":
        load_path = f"{model_id}.json"
        logger.info(f"Loading checkpoint from {load_path}")
        try:
            json_state = storage_client.read_file(MODEL_CHECKPOINT_BUCKET, load_path)
            state = json.loads(json_state.decode("utf-8"))
            model = cls(
                model_id=state["model_id"],
                elements=[Element.from_dict(v) for v in state["elements"].values()],
                storage_client=storage_client,
                alpha=state["alpha"],
                beta=state["beta"],
            )
            logger.info(f"Successfully loaded model checkpoint from {load_path}")
            return model
        except StorageException as e:
            logger.error(f"Model checkpoint not found for {model_id}")
            raise e

    def get_stats(self) -> dict:
        stats = {"model_id": self.model_id}
        for element_id, element in self.elements.items():
            stats[element_id] = {
                "id": element_id,
                "success_rate": element.get_success_rate(),
                "impression": element.impression,
                "success_count": element.success_count,
                "status": element.status,
                "creation_time": element.creation_time.isoformat(),
                "last_updated_time": element.last_updated_time.isoformat(),
            }
        return stats
