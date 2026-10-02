from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.db import get_db
from backend.app.schemas.resource import ResourceCreate, ResourceResponse
from backend.app.services.resource_service import get_resources, create_resource

router = APIRouter()

@router.get("/", response_model=list[ResourceResponse])
async def list_resources(db: AsyncSession = Depends(get_db)):
    return await get_resources(db)


@router.post("/", response_model=ResourceResponse)
async def create_resource_route(payload: ResourceCreate, db: AsyncSession = Depends(get_db)):
    return await create_resource(db, payload.model_dump())
