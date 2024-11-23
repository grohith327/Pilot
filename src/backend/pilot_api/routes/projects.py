from fastapi import APIRouter

router = APIRouter(prefix="/projects", tags=["projects"])

@router.post("/create")
async def create_project():
    pass

@router.get("/{project_id}")
async def get_project(project_id: str):
    pass

@router.put("/{project_id}")
async def update_project(project_id: str):
    pass

@router.post("/{project_id}/elements")
async def add_element_to_project(project_id: str, element_id: str):
    pass
