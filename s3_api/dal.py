import asyncio
import logging
from contextlib import asynccontextmanager
from fastapi import UploadFile

from botocore.exceptions import ClientError
from aiobotocore.session import get_session

import global_config

logger = logging.getLogger('uvicorn.error')


class S3Client:
    # config = {
    #     'aws_access_key_id': global_config.AWS_ACCESS_KEY_ID,
    #     'aws_secret_access_key': global_config.AWS_SECRET_ACCESS_KEY,
    #     'endpoint_url': global_config.S3_URL,
    #     'region_name': 'us-east-1',
    # }
    session = get_session()
    bucket_name = global_config.BUCKET_NAME

    @asynccontextmanager
    async def _get_client(self):
        try:
            async with self.session.create_client('s3', aws_access_key_id='minioadmin',
                                                  aws_secret_access_key='minioadmin',
                                                  endpoint_url='http://127.0.0.1:9000',
                                                  region_name='us-east-1') as client:
                yield client
        except Exception as err:
            logger.error(f'Error creating S3 client: {err}')

    async def upload_file(self, file: UploadFile):
        object_name = file.filename
        logger.info('step1')
        try:
            async with self._get_client() as client:
                logger.info('step2')
                file_content = await file.read()
                logger.info('step3')
                await client.put_object(Bucket=self.bucket_name, Key=object_name, Body=file_content)
                logger.info(f'File {object_name} uploaded successfully')
        except ClientError as err:
            logger.error(f'Error uploading file {object_name}: {err}')
