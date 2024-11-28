from fastapi import FastAPI
from pilot_api.routes import health, projects, elements

app = FastAPI(title="Pilot API", version="0.1.0")

app.include_router(health.router)
app.include_router(projects.router)
app.include_router(elements.router)
