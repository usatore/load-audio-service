import shutil
import os

from fastapi import APIRouter, UploadFile, Depends
from app.audiofiles.dao import AudiofilesDAO
from app.users.models import Users
from app.users.dependencies import get_current_user


router = APIRouter(prefix="/audiofiles", tags=["Работа с аудиофайлами"])

@router.post("/load", status_code=201)
async def add_audiofile(
        filename: str,
        file: UploadFile,
        user: Users = Depends(get_current_user)
):
    user_folder = f"storage/user_{user.id}"
    os.makedirs(user_folder, exist_ok=True)
    filepath = os.path.join(user_folder, f"{filename}.mp3")

    with open(filepath, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)

    await AudiofilesDAO.add(filename=filename, filepath=filepath, user_id=user.id)

    return {"message": "Файл успешно загружен"}


@router.get("")
async def get_audiofiles(
    user: Users = Depends(get_current_user)
):
    return await AudiofilesDAO.find_all(user_id=user.id)

