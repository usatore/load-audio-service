from app.dao.base import BaseDAO
from app.audiofiles.models import Audiofiles

class AudiofilesDAO(BaseDAO):
    model = Audiofiles

    @classmethod
    async def add(
            cls,
            filename: str,
            filepath: str,
            user_id: int,
    ):