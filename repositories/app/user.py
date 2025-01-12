"""Repository layer for user module"""

from uuid import UUID
from sqlalchemy.orm import Session
from domain import models, schemas, errors
from utils.hasher import Hasher


def get_users(session: Session) -> list[models.User]:
    """Get all users"""
    query = session.query(models.User).all()
    return query


def get_user_by_id(session: Session, user_id: UUID) -> models.User:
    """Get user by uuid"""
    query = session.query(models.User).where(user_id == models.User.id).first()
    if query is None:
        raise errors.ResourceNotFoundError(resource=f"User with UUID {user_id}")
    return query


def get_user_by_email(session: Session, user_email: UUID) -> models.User:
    """Get user by email"""
    query = session.query(models.User).where(user_email == models.User.email).first()
    if query is None:
        raise errors.ResourceNotFoundError(resource=f"User with email {user_email}")
    return query


def create_user(session: Session, user_input: schemas.UserInput) -> models.User:
    """Create user"""
    user = models.User.from_input(user_input=user_input)

    session.add(user)
    session.flush()
    return user


def edit_user(
    session: Session, user_id: UUID, user_edit: schemas.UserEdit
) -> models.User:
    """Edit user by uuid"""

    user = get_user_by_id(session=session, user_id=user_id)
    user_dict = user_edit.model_dump(exclude_unset=True)

    for key, value in user_dict.items():
        setattr(user, key, value)

    session.flush()
    return user


def delete_user(session: Session, user_id: UUID) -> models.User:
    """Edit user by uuid"""

    user = get_user_by_id(session=session, user_id=user_id)

    session.delete(user)
    session.flush()
    return user


def validate_user_login(
    session: Session, login_input: schemas.LoginInput
) -> models.User:
    """Returns the user model if login is valid, raises UnauthorizedError error otherwise"""
    try:
        user = get_user_by_email(session=session, user_email=login_input.email)
        pwd_match = Hasher.verify_password(
            plain_password=login_input.password, hashed_password=user.password
        )
        if not pwd_match:
            raise errors.UnauthorizedError()
        return user
    except (errors.ResourceNotFoundError, errors.UnauthorizedError):
        raise errors.UnauthorizedError(resource="Invalid email or password") from None


def add_user_mp_access_token(
    session: Session, user_id: UUID, access_token: str
) -> models.User:
    """Add MercadoPago access token to user"""
    user = get_user_by_id(session=session, user_id=user_id)
    user.mp_access_token = access_token
    session.flush()
    return user
