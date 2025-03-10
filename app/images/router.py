import shutil
from fastapi import APIRouter, UploadFile


router = APIRouter(
    prefix="/images",
    tags=["Download"]
)


@router.post("/hotels")
async def add_hotel_image(name: int, file: UploadFile):
    with open(f"app/static/images/{name}.webp", "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
