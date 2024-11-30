from supabase import create_client, Client


class StorageClient:
    def __init__(self, url: str, key: str):
        self.supabase_client: Client = create_client(url, key)

    def read_file(self, bucket_name: str, file_path: str):
        return self.supabase_client.storage.from_(bucket_name).download(file_path)

    def write_file(self, bucket_name: str, file_path: str, file_data):
        return self.supabase_client.storage.from_(bucket_name).upload(
            file_path, file_data
        )