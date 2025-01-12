"""Controllers for the login module"""

from typing import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from domain import schemas
from sqlalchemy.orm import Session
from config import get_session
from services.app import login as login_service
from .config import (
    LOGIN,
    router,
)


@router.post(
    path="/login",
    summary="Login a user in the application",
    tags=[LOGIN["name"]],
)
def login(
    login_form: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: Session = Depends(get_session),
) -> schemas.Token:
    """Login user on application, returning access token."""
    return login_service.authenticate_user(session=session, login_form=login_form)
