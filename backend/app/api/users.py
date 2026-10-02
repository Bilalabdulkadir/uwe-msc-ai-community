from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.db import get_db
from backend.app.models.models import User
from backend.app.schemas.user import UserCreate, UserResponse
from backend.app.core.security import hash_password
from backend.app.services.user_service import get_users, create_user

router = APIRouter()

@router.get("/", response_model=list[UserResponse])
async def list_users(db: AsyncSession = Depends(get_db)):
    return await get_users(db)


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user_route(payload: UserCreate, db: AsyncSession = Depends(get_db)):
    existing = (await db.execute(select(User).where(User.email == payload.email))).scalar_one_or_none()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    data = payload.model_dump()
    data["password_hash"] = hash_password(data.pop("password"))
    return await create_user(db, data)
