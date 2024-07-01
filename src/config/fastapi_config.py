from contextlib import asynccontextmanager

from aiobotocore.session import get_session
from fastapi import FastAPI
from loguru import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        session = get_session()
        yield {'s3session': session}
    except Exception as err:
        logger.info('Error creating session', err)
