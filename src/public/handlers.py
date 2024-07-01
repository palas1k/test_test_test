import logging

from fastapi import APIRouter, UploadFile, HTTPException, Depends
from starlette import status

from src.dependencies import get_s3client

logger = logging.getLogger('uvicorn.error')
memes_router = APIRouter()


@memes_router.post('/memes')
async def create_meme(file: UploadFile,  client=Depends(get_s3client)):
    try:
        await client.upload_file(file)
    except Exception as err:
        logger.error("Meme upload failed", err)
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Error uploading')
