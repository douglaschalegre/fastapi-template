from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from domain import schemas
from repositories.app import user as user_repositories
from utils import jwt_token as jwt


def authenticate_user(session: Session, login_form: OAuth2PasswordRequestForm) -> schemas.Token:
    """Login user on application"""
    login_input = schemas.LoginInput(email=login_form.username, password=login_form.password)
    user = user_repositories.validate_user_login(session=session, login_input=login_input)

    if user:
        access_token = jwt.create_access_token(user_id=user.id)

    return schemas.Token(access_token=access_token, token_type='bearer', user_id=user.id)
