import logging
import random

from fastapi import APIRouter, UploadFile, HTTPException, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.config.db import get_session
from src.database.crud import FileMethods
from src.dependencies import get_s3client

logger = logging.getLogger('uvicorn.error')
memes_router = APIRouter()


@memes_router.post('/memes')
async def create_meme(file: UploadFile, client=Depends(get_s3client)):
    try:
        await client.upload_file(file)
    except Exception as err:
        logger.error("Meme upload failed", err)
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Error uploading')


@memes_router.post('/testpsql')
async def test_psql(file: UploadFile, session: AsyncSession = Depends(get_session)):
    client = FileMethods(session=session)
    logger.info("CLIENT", client)
    await client.create_file(name=file.filename, link='link')
    return {'success': True}
