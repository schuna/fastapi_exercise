from fastapi import APIRouter, File, UploadFile, Depends
import shutil
# noinspection PyUnresolvedReferences,PyPackageRequirements
import pytesseract

from utils import log

router = APIRouter(
    prefix='/ocr',
    tags=['ocr'],
    dependencies=[Depends(log)]
)


@router.post('/')
def ocr(image: UploadFile = File(...)):
    filepath = 'txtFile'
    with open(filepath, 'w+b') as wf:
        shutil.copyfileobj(image.file, wf)
    return pytesseract.image_to_string(filepath, lang='eng')
