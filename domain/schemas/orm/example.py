'''ORM schema for Example sqlalchemy model'''
from datetime import datetime
from uuid import UUID
from pydantic import Field
from domain.schemas.generic import TableSchema


class ExampleEdit(TableSchema):
    '''Edit Example schema'''


class ExampleInput(ExampleEdit):
    '''Input Example schema'''


class ExampleLite(ExampleInput):
    '''Lite Example schema'''
    id: UUID = Field(title='UUID')
    created_at: datetime = Field(title='Example creation datetime in UTC 0')


class ExampleBase(ExampleLite):
    '''Base Example schema'''
    data: dict = Field(default=None, title='Example data')
