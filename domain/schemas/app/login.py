"""Login schema"""

from uuid import UUID
from pydantic import BaseModel
from domain.schemas.generic import GenericSchema


class LoginInput(GenericSchema):
    """Data required to user login"""

    email: str
    password: str


class Token(BaseModel):
    """Login response schema"""

    access_token: str
    token_type: str
    user_id: UUID
