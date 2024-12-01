import uuid
from datetime import datetime
import os


SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_ANON_KEY")
MODEL_CHECKPOINT_BUCKET = os.getenv("MODEL_CHECKPOINT_BUCKET")
STAGE = os.getenv("STAGE")

PROJECTS_TABLE = "projects"
ELEMENTS_TABLE = "elements"


def is_string_empty(string: str) -> bool:
    return string is None or string.strip() == ""


def is_valid_uuid(uuid_to_test: str) -> bool:
    try:
        uuid.UUID(uuid_to_test)
        return True
    except ValueError:
        return False


def get_current_time() -> str:
    return datetime.now().isoformat()


def generate_uuid() -> str:
    return str(uuid.uuid4())
