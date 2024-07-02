from sqlalchemy import update, delete, and_, select
from sqlalchemy.ext.asyncio import AsyncSession
from loguru import logger

from src.database.models import File


class FileMethods:
    def __init__(self, session=AsyncSession):
        self.session = session

    async def _commit(self, quere):
        logger.info(self.session)
        await self.session.add(quere)
        result = await self.session.commit()
        logger.info("RESULT", result)
        return result

    async def create_file(self, name: str, link: str):
        try:
            logger.info("CREATE QUERE")
            quere = File(name=name, link=link)
            logger.info("Quere %s:", quere)
            await self._commit(quere)
            return True
        except Exception as err:
            return

    async def get_file(self, name: str):
        try:
            quere = select(File(name == name))
            result = await self._commit(quere)
        except Exception as err:
            return

    async def update_file(self, name: str, link: str):
        try:
            quere = update(File).where(name == name).values(link=link, name=name)
            result = await self._commit(quere)
        except Exception as err:
            return

    async def delete_file(self, name: str):
        try:
            quere = delete(File).where(name == name)
            await self.session.execute(quere)
            await self.session.commit()
            return True
        except Exception as err:
            return
