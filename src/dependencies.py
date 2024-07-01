import logging

from botocore.exceptions import ClientError
from fastapi import Request
from src.s3_api.s3client import S3Client

from src.config import config


logger = logging.getLogger(__name__)


async def get_s3client(request: Request):
    try:
        s3session = request.state.s3session
        async with s3session.create_client('s3',
                                           aws_access_key_id=config.AWS_ACCESS_KEY_ID,
                                           aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY,
                                           endpoint_url=config.S3_URL,
                                           use_ssl=False) as client:
            yield S3Client(client)
    except ClientError as err:
        logger.warning("Failed to create S3 client", err)
