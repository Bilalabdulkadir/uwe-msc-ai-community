from fastapi import APIRouter, Depends
from typing import List
from ..schemas.project import ProjectRead
from ..services.project_service import get_projects
from ..db import get_session
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

@router.get('/', response_model=List[ProjectRead])
async def list_projects(session: AsyncSession = Depends(get_session)):
    return await get_projects(session)
