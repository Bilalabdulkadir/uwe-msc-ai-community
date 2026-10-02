from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from ..models.models import User

async def get_users(session: AsyncSession):
    q = await session.execute(select(User).limit(50))
    users = q.scalars().all()
    results = []
    for u in users:
        results.append({
            "id": u.id,
            "username": u.username,
            "email": u.email,
            "role": u.role.value if hasattr(u.role, 'value') else str(u.role),
            "created_at": u.created_at,
        })
    return results
