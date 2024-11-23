import uuid

def is_valid_uuid(uuid_to_test: str) -> bool:
    try:
        uuid.UUID(uuid_to_test)
        return True
    except ValueError:
        return False
