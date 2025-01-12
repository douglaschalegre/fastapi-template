"""ORM schema for User sqlalchemy model"""

from datetime import datetime, date
from uuid import UUID
from pydantic import Field
from domain.schemas.generic import TableSchema
from enum import Enum


class SexEnum(str, Enum):
    """User sex options"""

    male = 'male'
    female = 'female'


class UserEdit(TableSchema):
    """Edit User schema"""

    name: str | None = Field(default=None)
    phone: str | None = Field(default=None)
    email: str | None = Field(default=None)
    password: str | None = Field(default=None)
    sex: SexEnum | None = Field(default=None)
    birthdate: date | None = Field(default=None)


class UserInput(UserEdit):
    """Input User schema"""

    name: str = Field()
    email: str = Field()
    password: str = Field()
    sex: SexEnum = Field()
    birthdate: date = Field()


class UserLite(UserInput):
    """Lite User schema"""

    id: UUID = Field(title='UUID')
    phone_confirmed: bool = Field(default=False)
    email_confirmed: bool = Field(default=False)
    created_at: datetime = Field(title='User creation datetime in UTC 0')
    updated_at: datetime = Field(title='User update datetime in UTC 0')
    password: str | None = Field(exclude=True)


class UserBase(UserLite):
    """Base User schema"""
