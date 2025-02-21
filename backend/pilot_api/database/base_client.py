from supabase import create_client, Client
from abc import ABC, abstractmethod


class BaseDbClient(ABC):
    def __init__(self, url: str, key: str, table_name: str):
        self.supabase_client: Client = create_client(url, key)
        self.table_name = table_name

    @abstractmethod
    def fetch_data(self, query):
        pass

    @abstractmethod
    def update_data(self, query, data):
        pass

    @abstractmethod
    def insert_data(self, data):
        pass

    def _validate_data(self, data):
        assert "id" in data, "id is required"
        self._validate_id(data["id"])

        assert "name" in data, "name is required"
        self._validate_name(data["name"])
