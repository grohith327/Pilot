from pilot_api.database.base_client import BaseDbClient
import logging

logger = logging.getLogger(__name__)


class ProjectDbClient(BaseDbClient):
    _instance = None

    def __init__(self, url: str, key: str):
        super().__init__(url, key, "projects")

    def fetch_data(self, query):
        try:
            self._validate_id(query.id)
            return (
                self.supabase_client.table(self.table_name)
                .select("*")
                .eq("id", query.id)
                .execute()
            )
        except AssertionError as e:
            logger.error(f"Invalid id: {query.id} to query data: {e}")
            raise e
        except Exception as e:
            logger.error(f"Error fetching project data: {e}")
            raise e

    def update_data(self, query, data):
        try:
            self._validate_id(query.id)
            return (
                self.supabase_client.table(self.table_name)
                .update(data)
                .eq("id", query.id)
                .execute()
            )
        except AssertionError as e:
            logger.error(f"Invalid id: {query.id} to update data: {e}")
            raise e
        except Exception as e:
            logger.error(f"Error updating project data: {e}")
            raise e

    def insert_data(self, data):
        try:
            self._validate_data(data)
            return self.supabase_client.table(self.table_name).insert(data).execute()
        except AssertionError as e:
            logger.error(f"Invalid data: {data} to perform insert operation: {e}")
            raise e
        except Exception as e:
            logger.error(f"Error inserting project data: {e}")
            raise e

    @classmethod
    def get_instance(cls, url: str, key: str):
        if cls._instance is None:
            cls._instance = cls(url, key)
        return cls._instance
