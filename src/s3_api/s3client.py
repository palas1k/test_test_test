from fastapi import UploadFile

from botocore.exceptions import ClientError

from src.config import config

from loguru import logger


class S3Client:
    def __init__(self, client):
        self.client = client
        self.bucket_name = config.BUCKET_NAME

    async def _check_bucket(self):
        try:
            await self.client.get_bucket(self.bucket_name)
        except Exception as err:
            logger.error(f'Bucket with name {self.bucket_name} not found, create or update bucket name')

    async def upload_file(self, file: UploadFile):
        await self._check_bucket()
        object_name = file.filename
        try:
            file_content = await file.read()
            uploaded_file = await self.client.put_object(Bucket=self.bucket_name, Key=object_name, Body=file_content)
        except ClientError as err:
            logger.error(f'Error uploading file {object_name}: {err}')
