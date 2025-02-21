from pilot_api.database.base_client import BaseDbClient
from pilot_api.utils import ELEMENTS_TABLE
import logging

logger = logging.getLogger(__name__)


class ElementDbClient(BaseDbClient):
    _instance = None

    def __init__(self, url: str, key: str):
        super().__init__(url, key, ELEMENTS_TABLE)

    def fetch_data(self, query):
        return (
            self.supabase_client.table(self.table_name)
            .select("*")
            .eq("id", query["id"])
            .execute()
        )

    def fetch_with_filters(self, key: str, filter: str):
        return (
            self.supabase_client.table(self.table_name)
            .select("*")
            .eq(key, filter)
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
