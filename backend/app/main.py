from fastapi import FastAPI
from .api import health, users, profiles, discussions, comments, events, projects, resources, publications, mentorships, notifications

app = FastAPI(
    title="UWE MSc AI Community API",
    version="0.1.0",
    description="Backend API for the UWE MSc AI Community Platform",
)

app.include_router(health.router)
app.include_router(users.router, prefix="/api/users", tags=["users"])
app.include_router(profiles.router, prefix="/api/profiles", tags=["profiles"])
app.include_router(discussions.router, prefix="/api/discussions", tags=["discussions"])
app.include_router(comments.router, prefix="/api/comments", tags=["comments"])
app.include_router(events.router, prefix="/api/events", tags=["events"])
app.include_router(projects.router, prefix="/api/projects", tags=["projects"])
app.include_router(resources.router, prefix="/api/resources", tags=["resources"])
app.include_router(publications.router, prefix="/api/publications", tags=["publications"])
app.include_router(mentorships.router, prefix="/api/mentorships", tags=["mentorships"])
app.include_router(notifications.router, prefix="/api/notifications", tags=["notifications"])

@app.get("/")
async def root():
    return {"message": "UWE MSc AI Community API", "status": "ok"}
