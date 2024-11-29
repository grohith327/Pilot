from pilot_api.database.base_client import BaseDbClient
import logging

logger = logging.getLogger(__name__)


class ProjectDbClient(BaseDbClient):
    _instance = None

    def __init__(self, url: str, key: str):
        super().__init__(url, key, "projects")

    def fetch_data(self, query):
        return (
            self.supabase_client.table(self.table_name)
            .select("*")
            .eq("id", query["id"])
            .execute()
        )

    def update_data(self, query, data):
        return (
            self.supabase_client.table(self.table_name)
            .update(data)
            .eq("id", query["id"])
            .execute()
        )

    def insert_data(self, data):
        return self.supabase_client.table(self.table_name).insert(data).execute()

    @classmethod
    def get_instance(cls, url: str, key: str):
        if cls._instance is None:
            cls._instance = cls(url, key)
        return cls._instance
