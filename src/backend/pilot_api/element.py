from datetime import datetime


class Element:
    def __init__(
        self,
        id: str,
        name: str,
        description: str,
        impression: int = 0,
        success_count: int = 0,
        is_active: bool = True,
    ):
        self.id = id
        self.name = name
        self.description = description
        self.impression = impression
        self.success_count = success_count
        self.creation_time = datetime.now()
        self.last_updated_time = datetime.now()
        self.is_active = is_active

    def get_success_rate(self) -> float:
        if self.impression == 0:
            return 0.0
        return self.success_count / self.impression

    def update_success_count(self, success: bool):
        self.impression += 1
        if success:
            self.success_count += 1
        self.last_updated_time = datetime.now()

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "impression": self.impression,
            "success_count": self.success_count,
            "creation_time": self.creation_time.isoformat(),
            "last_updated_time": self.last_updated_time.isoformat(),
            "is_active": self.is_active,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Element":
        element = cls(
            id=data["id"],
            name=data["name"],
            description=data["description"],
            impression=data["impression"],
            success_count=data["success_count"],
        )
        element.creation_time = datetime.fromisoformat(data["creation_time"])
        element.last_updated_time = datetime.fromisoformat(data["last_updated_time"])
        element.is_active = data["is_active"]
        return element
    