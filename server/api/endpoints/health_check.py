from fastapi import APIRouter

from core.logger import logger

router = APIRouter()


@router.get('/health-check')
def read_root():
    logger.info('Health check')
    return {'msg': 'ok'}
