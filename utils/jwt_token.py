from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from uuid import UUID
from config.env import jwt_secret_key
from domain import errors

SECRET_KEY = jwt_secret_key
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_HOURS = 4


def is_token_expired(expiration: int) -> bool:
    return datetime.now(timezone.utc) > datetime.fromtimestamp(expiration, tz=timezone.utc)


def create_access_token(user_id: UUID) -> str:
    """Create a new JWT access token."""
    data = {'sub': str(user_id)}
    to_encode = data
    expire = datetime.now(timezone.utc) + timedelta(hours=ACCESS_TOKEN_EXPIRE_HOURS)
    to_encode.update({'exp': expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def decode_access_token(token: str) -> dict:
    """Decode a JWT access token."""
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise errors.BadRequestError(
            resource='Authorization token could not be decoded.'
        ) from JWTError
