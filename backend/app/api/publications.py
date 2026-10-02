from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.db import get_db
from backend.app.schemas.publication import PublicationCreate, PublicationResponse
from backend.app.services.publication_service import get_publications, create_publication

router = APIRouter()

@router.get("/", response_model=list[PublicationResponse])
async def list_publications(db: AsyncSession = Depends(get_db)):
    return await get_publications(db)


@router.post("/", response_model=PublicationResponse)
async def create_publication_route(payload: PublicationCreate, db: AsyncSession = Depends(get_db)):
    return await create_publication(db, payload.model_dump())
