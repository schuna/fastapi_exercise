from fastapi import APIRouter, File, UploadFile
import shutil
from fastapi.responses import FileResponse

router = APIRouter(
    prefix='/file',
    tags=["file"]
)


@router.post("/file")
def get_file(file: bytes = File(...)):
    content = file.decode('utf-8')
    lines = content.split('\n')
    return {'lines': lines}


@router.post("/upload_file")
def get_upload_file(upload_file: UploadFile = File(...)):
    path = f"files/{upload_file.filename}"
    with open(path, 'w+b') as wf:
        shutil.copyfileobj(upload_file.file, wf)
    return {
        'filename': path,
        'type': upload_file.content_type
    }


@router.post("/download/{name}", response_class=FileResponse)
def download_file(name: str):
    path = f'files/{name}'
    return path
