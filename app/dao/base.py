from sqlalchemy import select
from app.database import async_session_maker


class BaseDAO:
    model = None

    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            # query = select(cls.model.__table__.columns).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().all()
            # return result.mappings().all()