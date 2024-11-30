from fastapi import FastAPI
from pilot_api.routes import health, projects, elements
from supabase import create_client
from pilot_api.utils import SUPABASE_URL, SUPABASE_KEY
from pilot_api.storage_client import StorageClient
from pilot_api.database.project_database import ProjectDbClient
from pilot_api.model.model_manager import ModelManager
import logging

logger = logging.getLogger(__name__)

app = FastAPI(title="Pilot API", version="0.1.0")
storage_client = StorageClient.get_instance(SUPABASE_URL, SUPABASE_KEY)
project_db_client = ProjectDbClient.get_instance(SUPABASE_URL, SUPABASE_KEY)
model_manager = ModelManager.get_instance(storage_client, project_db_client)

app.include_router(health.router)
app.include_router(projects.router)
app.include_router(elements.router)


@app.on_event("startup")
async def startup_event():
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    pk_response = supabase.rpc("get_primary_keys", {"table_name": "projects"}).execute()
    logger.warning(f"Loading models for {len(pk_response.data)} projects")
    for pk in pk_response.data:
        model_manager.load_model(pk)
    logger.warning("Successfully loaded models")
