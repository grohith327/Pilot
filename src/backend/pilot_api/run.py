import logging
import uvicorn
from dotenv import load_dotenv
from datetime import datetime
from fastapi import FastAPI

load_dotenv()

from pilot_api.routes import health, projects, elements
from supabase import create_client
from pilot_api.utils import SUPABASE_URL, SUPABASE_KEY
from pilot_api.storage_client import StorageClient
from pilot_api.database.project_database import ProjectDbClient
from pilot_api.model.model_manager import ModelManager


def setup_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(f"app-{datetime.now().strftime('%Y-%m-%d')}.log"),
            logging.StreamHandler(),
        ],
    )
    logger = logging.getLogger()
    return logger


logger = setup_logging()

app = FastAPI(title="Pilot API", version="0.1.0")
storage_client = StorageClient.get_instance(SUPABASE_URL, SUPABASE_KEY)
project_db_client = ProjectDbClient.get_instance(SUPABASE_URL, SUPABASE_KEY)
model_manager = ModelManager.get_instance(storage_client, project_db_client)


@app.on_event("startup")
async def startup_event():
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    pk_response = supabase.rpc("get_primary_keys", {"table_name": "projects"}).execute()
    logger.warning(f"Loading models for {len(pk_response.data)} projects")
    for pk in pk_response.data:
        model_manager.load_model(pk)
    logger.warning("Successfully loaded models")


app.include_router(health.router)
app.include_router(projects.router)
app.include_router(elements.router)


def main():
    uvicorn.run("pilot_api.run:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
