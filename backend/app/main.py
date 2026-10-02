from fastapi import FastAPI
from .api import health, users, events, projects, resources, discussions

app = FastAPI(title="UWE MSc AI Community API")

app.include_router(health.router)
app.include_router(users.router, prefix="/api/users", tags=["users"])
app.include_router(events.router, prefix="/api/events", tags=["events"])
app.include_router(projects.router, prefix="/api/projects", tags=["projects"])
app.include_router(resources.router, prefix="/api/resources", tags=["resources"])
app.include_router(discussions.router, prefix="/api/discussions", tags=["discussions"])

@app.get("/")
async def root():
    return {"message": "UWE MSc AI Community API"}
