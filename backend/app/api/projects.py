from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.db import get_db
from backend.app.schemas.project import ProjectCreate, ProjectResponse
from backend.app.services.project_service import get_projects, create_project

router = APIRouter()

@router.get("/", response_model=list[ProjectResponse])
async def list_projects(db: AsyncSession = Depends(get_db)):
    return await get_projects(db)


@router.post("/", response_model=ProjectResponse)
async def create_project_route(payload: ProjectCreate, db: AsyncSession = Depends(get_db)):
    owner_id = "11111111-1111-4111-8111-111111111111"
    return await create_project(db, payload.model_dump(), owner_id)
