"""Controllers for the user module"""

from fastapi import Depends, Path, Body
from typing import Annotated
from sqlalchemy.orm import Session
from uuid import UUID
from config import get_session
from services.app import auth as auth_service
from services.app import user as user_service
from domain import schemas, models
from .config import (
    USER,
    router,
)

USER_ID_DESCRIPTION = 'UUID that represents the user'


@router.get(
    path='/users',
    summary='Get all users',
    tags=[USER['name']],
    response_model=list[schemas.User],
)
def get_users(
    authenticated_user: Annotated[str, Depends(auth_service.user_auth)],
    session: Session = Depends(get_session),
) -> list[models.User]:
    """Get all users"""
    return user_service.get_users(session=session)


@router.get(
    path='/user/{user_id}',
    summary='Get user by uuid',
    tags=[USER['name']],
    response_model=schemas.User,
)
def get_user_by_id(
    authenticated_user: Annotated[str, Depends(auth_service.user_auth)],
    session: Session = Depends(get_session),
    user_id: UUID = Path(description=USER_ID_DESCRIPTION),
) -> models.User:
    """Get user by uuid"""
    return user_service.get_user_by_id(session=session, user_id=user_id)


@router.post(
    path='/user',
    summary='Create a new user',
    tags=[USER['name']],
    response_model=schemas.User,
)
def create_user(
    session: Session = Depends(get_session),
    user_input: schemas.UserInput = Body(description='User creation schema'),
) -> models.User:
    """Create a new user"""
    return user_service.create_user(session=session, user_input=user_input)


@router.patch(
    path='/user/{user_id}',
    summary='Update user',
    tags=[USER['name']],
    response_model=schemas.User,
)
def edit_user(
    authenticated_user: Annotated[str, Depends(auth_service.user_auth)],
    session: Session = Depends(get_session),
    user_id: UUID = Path(description=USER_ID_DESCRIPTION),
    user_edit: schemas.UserEdit = Body(description='User edition schema'),
) -> models.User:
    """Update user"""
    return user_service.edit_user(
        session=session, user_id=user_id, user_edit=user_edit, authenticated_user=authenticated_user
    )
