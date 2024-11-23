from fastapi import APIRouter

router = APIRouter(prefix="/elements", tags=["elements"])


@router.post("/create")
async def create_element():
    pass


@router.get("/{element_id}")
async def get_element(element_id: str):
    pass


@router.put("/{element_id}")
async def update_element(element_id: str):
    pass
