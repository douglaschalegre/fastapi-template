'''ORM schema for Child sqlalchemy model'''
from datetime import datetime
from uuid import UUID
from pydantic import Field
from domain.schemas.generic import TableSchema


class ChildLite(TableSchema):
    '''Lite Child schema'''
    id: UUID = Field(title='UUID of the adjacent task and task link')
    example_id: UUID = Field(title='UUID of the parent task')
    created_at: datetime = Field(title='Child creation datetime in UTC 0')


class ChildBase(ChildLite):
    '''Base Child schema'''
    data: dict = Field(default=None, title='Child data')
