"""Model for user"""

from __future__ import annotations
from uuid import uuid4
from sqlalchemy import Column, DateTime, Text, Boolean, Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import functions
from .generic import GenericBase
from domain.schemas import UserInput
from utils.hasher import Hasher


class User(GenericBase):
    """User model"""

    __tablename__ = "user"

    id = Column("user_id", UUID(as_uuid=True), default=uuid4, primary_key=True)
    name = Column("user_name", Text, nullable=False)
    phone = Column("user_phone", Text, nullable=True)
    phone_confirmed = Column("user_phone_confirmed", Boolean, nullable=False)
    email = Column("user_email", Text, nullable=False)
    email_confirmed = Column("user_email_confirmed", Boolean, nullable=False)
    password = Column("user_password", Text, nullable=False)
    birthdate = Column("user_birthdate", Date, nullable=False)
    sex = Column("user_sex", Text, nullable=False)
    created_at = Column("user_created_at", DateTime, default=functions.now())
    updated_at = Column(
        "user_updated_at", DateTime, default=functions.now(), onupdate=functions.now()
    )

    @staticmethod
    def from_input(user_input: UserInput) -> User:
        """Build user model from input schema"""
        return User(
            name=user_input.name,
            phone=user_input.phone,
            phone_confirmed=False,
            email=user_input.email,
            email_confirmed=False,
            password=Hasher.get_password_hash(user_input.password),
            birthdate=user_input.birthdate.strftime("%Y-%m-%d"),
            sex=user_input.sex.value,
        )
