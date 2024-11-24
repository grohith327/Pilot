import uuid
from datetime import datetime


def is_valid_uuid(uuid_to_test: str) -> bool:
    try:
        uuid.UUID(uuid_to_test)
        return True
    except ValueError:
        return False


def get_current_time() -> datetime:
    return datetime.now()


def generate_uuid() -> str:
    return str(uuid.uuid4())
