from app.dao.base import BaseDAO
from app.audiofiles.models import Audiofiles
from app.database import async_sessionmaker
from sqlalchemy import insert

class AudiofilesDAO(BaseDAO):
    model = Audiofiles

    @classmethod
    async def add(
            cls,
            filename: str,
            filepath: str,
            user_id: int,
    ):

        async with async_sessionmaker() as session:

            add_audiofile = (
                insert(Audiofiles)
                .values(
                    filename=filename,
                    filepath=filepath,
                    user_id=user_id,
                )
            )

            await session.execute(add_audiofile)
            await session.commit()


