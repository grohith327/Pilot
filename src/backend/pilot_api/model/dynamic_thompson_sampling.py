from pilot_api.model.base_bandit_algorithm import BanditAlgorithm
from pilot_api.element import Element
import numpy as np
import json
import logging
import uuid
import os

logger = logging.getLogger(__name__)


class DynamicThompsonSampling(BanditAlgorithm):
    def __init__(self, elements: list[Element], alpha: float = 1.0, beta: float = 1.0):
        self.alpha = alpha
        self.beta = beta
        self.elements = {}
        self.model_id = uuid.uuid4()

        self.add_elements(elements)

    def add_elements(self, new_elements: list[Element]):
        if len(self.elements) != 0:
            active_elements = [
                element for element in self.elements.values() if element.is_active
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
                self.elements[new_element.id].is_active = True
        logger.warning(f"Added {len(new_elements)} elements to the algorithm")

    def remove_elements(self, elements_to_remove: list[Element]):
        for element_to_remove in elements_to_remove:
            if element_to_remove.id in self.elements:
                self.elements[element_to_remove.id].is_active = False
        logger.warning(f"Removed {len(elements_to_remove)} elements from the algorithm")

    def get_recommendation(self) -> str:
        active_elements = {k: v for k, v in self.elements.items() if v.is_active}
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

    def save_checkpoint(self, checkpoint_path: str):
        state = {
            "elements": {k: v.to_dict() for k, v in self.elements.items()},
            "alpha": self.alpha,
            "beta": self.beta,
            "model_id": self.model_id,
        }

        save_path = os.path.join(checkpoint_path, f"{self.model_id}.json")
        logger.info(f"Saving checkpoint to {save_path}")
        with open(save_path, "w") as f:
            json.dump(state, f)

    def load_from_checkpoint(self, checkpoint_path: str, model_id: str):
        load_path = os.path.join(checkpoint_path, f"{model_id}.json")
        logger.info(f"Loading checkpoint from {load_path}")
        with open(load_path, "r") as f:
            state = json.load(f)

        self.elements = {k: Element.from_dict(v) for k, v in state["elements"].items()}
        self.alpha = state["alpha"]
        self.beta = state["beta"]
        self.model_id = state["model_id"]

    def get_stats(self) -> dict:
        stats = {"model_id": self.model_id}
        for element_id, element in self.elements.items():
            stats[element_id] = {
                "id": element_id,
                "success_rate": element.get_success_rate(),
                "impression": element.impression,
                "success_count": element.success_count,
                "is_active": element.is_active,
                "creation_time": element.creation_time.isoformat(),
                "last_updated_time": element.last_updated_time.isoformat(),
            }
        return stats
