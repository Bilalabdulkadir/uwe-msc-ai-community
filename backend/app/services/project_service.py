from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.models.models import Project


async def get_projects(db: AsyncSession):
    result = await db.execute(select(Project).order_by(Project.created_at.desc()).limit(50))
    return result.scalars().all()


async def create_project(db: AsyncSession, payload: dict, owner_id):
    project = Project(**payload, owner_id=owner_id)
    db.add(project)
    await db.commit()
    await db.refresh(project)
    return project
