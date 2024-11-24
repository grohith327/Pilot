from fastapi import APIRouter
import os
from pilot_api.database.element_database import ElementDbClient


router = APIRouter(prefix="/elements", tags=["elements"])

URL = os.getenv("SUPABASE_URL")
KEY = os.getenv("SUPABASE_ANON_KEY")
element_db_client = ElementDbClient.get_instance(URL, KEY)


@router.post("/create")
async def create_element():
    pass


@router.get("/{element_id}")
async def get_element(element_id: str):
    pass


@router.put("/{element_id}")
async def update_element(element_id: str):
    pass
