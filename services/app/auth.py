from fastapi import Depends
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from domain import models, errors
from repositories.app import user as user_repositories
from utils.jwt_token import decode_access_token, is_token_expired
from config import get_session


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')


def user_auth(
    token: Annotated[str, Depends(oauth2_scheme)],
    session: Session = Depends(get_session),
) -> models.User:
    decoded_token = decode_access_token(token=token)
    expiration = decoded_token.get('exp')
    user_id = decoded_token.get('sub')
    if not user_id or not expiration:
        raise errors.ForbiddenRequestError(resource='Invalid authorization token')

    if is_token_expired(decoded_token['exp']):
        raise errors.ForbiddenRequestError(resource='Invalid authorization token')

    try:
        user = user_repositories.get_user_by_id(session=session, user_id=user_id)
    except errors.ResourceNotFoundError:
        raise errors.ResourceNotFoundError(
            resource='During autenthication process, could not find user with provided id'
        ) from None
    return user
