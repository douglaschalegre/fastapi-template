"""Service layer for user module"""

from uuid import UUID
from sqlalchemy.orm import Session
from domain import models, schemas
from repositories.app import user as user_repository
from utils.hasher import Hasher


def get_users(session: Session) -> list[models.User]:
    """Get all users"""
    return user_repository.get_users(session=session)


def get_user_by_id(session: Session, user_id: UUID) -> models.User:
    """Get user by uuid"""
    return user_repository.get_user_by_id(session=session, user_id=user_id)


def create_user(session: Session, user_input: schemas.UserInput) -> models.User:
    """Create user"""
    return user_repository.create_user(session=session, user_input=user_input)


def edit_user(
    _authenticated_user: models.User,
    session: Session,
    user_id: UUID,
    user_edit: schemas.UserEdit,
) -> models.User:
    """Edit user by uuid"""

    if user_edit.password:
        user_edit.password = Hasher.get_password_hash(user_edit.password)

    return user_repository.edit_user(
        session=session,
        user_id=user_id,
        user_edit=user_edit,
    )


def delete_user(_authenticated_user: models.User, session: Session, user_id: UUID) -> models.User:
    """Delete user by uuid"""

    return user_repository.delete_user(session=session, user_id=user_id)
