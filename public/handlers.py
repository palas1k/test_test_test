import logging

from fastapi import APIRouter, UploadFile, HTTPException, File

from s3_api.dal import S3Client

logger = logging.getLogger('uvicorn.error')
memes_router = APIRouter()


@memes_router.post('/memes')
async def create_meme(file: UploadFile = File(...)):
    try:
        client = S3Client()
    except Exception as err:
        logger.error("Create_meme create client fail", err)
    try:
        await client.upload_file(file)
    except Exception as err:
        logger.error("Meme upload failed", err)
        return HTTPException(status_code=500, detail='Error uploading')
