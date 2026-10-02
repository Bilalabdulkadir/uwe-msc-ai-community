from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.db import get_db
from backend.app.models.models import Profile, User
from backend.app.schemas.profile import ProfileCreate, ProfileResponse
from backend.app.services.profile_service import get_profiles, create_profile

router = APIRouter()

@router.get("/", response_model=list[ProfileResponse])
async def list_profiles(db: AsyncSession = Depends(get_db)):
    return await get_profiles(db)


@router.post("/", response_model=ProfileResponse, status_code=status.HTTP_201_CREATED)
async def create_profile_route(payload: ProfileCreate, db: AsyncSession = Depends(get_db)):
    user = (await db.execute(select(User).where(User.email == "demo@uwe.ac.uk"))).scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="Default demo user not found")
    return await create_profile(db, payload.model_dump(), user.id)
