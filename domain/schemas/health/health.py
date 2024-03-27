'''Health schemas'''
from pydantic import Field
from domain.schemas.generic import TableSchema


class LivenessResponse(TableSchema):
    '''Liveness response schema'''
    status: str = Field(default='UP', title='Liveness status', example='UP')


class ReadinessResponse(TableSchema):
    '''Readiness response schema'''
    status: str = Field(default='UP', title='Readiness status', example='UP')
