"""Health service"""

from domain.schemas.health import health as health_schemas


def check_liveness():
    """Check liveness"""
    return health_schemas.LivenessResponse()


def check_readiness():
    """Check readiness"""
    return health_schemas.ReadinessResponse()
