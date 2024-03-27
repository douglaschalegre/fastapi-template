"""Health controller"""
from fastapi import APIRouter
from services.health import health as health_service
from domain.schemas.health import health as health_schemas

# Config - Health
# Could be a separated file if there was multiple files for health
router = APIRouter()

HEALTH = dict(
    name='Health checks',
    description='API to check health'
)
tags = [HEALTH]


@router.get(
    path='/health/liveness',
    summary='Check liveness',
    tags=[HEALTH['name']],
    response_model=health_schemas.LivenessResponse,
)
def check_liveness():
    '''Check liveness'''
    return health_service.check_liveness()


@router.get(
    path='/health/readiness',
    summary='Check readiness',
    tags=[HEALTH['name']],
    response_model=health_schemas.ReadinessResponse,
)
def check_readiness():
    '''Check readiness'''
    return health_service.check_readiness()
