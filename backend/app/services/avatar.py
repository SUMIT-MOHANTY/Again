import os
from pathlib import Path
from fastapi import UploadFile
from ..config import UPLOAD_DIR

def save_avatar(member_id: int, file: UploadFile) -> str:
    upload_path = Path(UPLOAD_DIR)
    upload_path.mkdir(parents=True, exist_ok=True)
    filename = f"{member_id}_{file.filename}"
    file_path = upload_path / filename
    with open(file_path, "wb") as buffer:
        while chunk := file.file.read(1024 * 1024):
            buffer.write(chunk)
    return str(file_path)
