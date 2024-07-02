from contextlib import asynccontextmanager, AsyncExitStack

from aiobotocore.session import get_session
from fastapi import FastAPI
from loguru import logger
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.crud import FileMethods


@asynccontextmanager
async def lifespan(app: FastAPI):
    session = get_session()
    # exit_stack = AsyncExitStack()
    # async with exit_stack:
    #     file_methods = await exit_stack.enter_async_context(FileMethods())
    yield {'session': session}
