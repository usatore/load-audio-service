from sqlalchemy import select, insert
from app.database import async_session_maker
from sqlalchemy.exc import SQLAlchemyError


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

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            # query = select(cls.model.__table__.columns).filter_by(**filter_by) В файле так
            result = await session.execute(query)
            return result.scalar_one_or_none()
            # return result.mappings().one_or_none()

    @classmethod
    async def add(cls, **data):
        try:
            async with async_session_maker() as session:
                query = insert(cls.model).values(**data).returning(cls.model.id)
                result = await session.execute(query)
                await session.commit()
                return result.mappings().first()
        except (SQLAlchemyError, Exception) as e:
            if isinstance(e, SQLAlchemyError):
                msg = "Database Exc: Cannot insert data into table"
            elif isinstance(e, Exception):
                msg = "Unknown Exc: Cannot insert data into table"

            # logger.error(msg, extra={"table": cls.model.__tablename__}, exc_info=True)
            return None