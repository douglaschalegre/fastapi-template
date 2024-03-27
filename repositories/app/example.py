'''Repository layer for example module'''
from sqlalchemy.orm import Session

from domain import (
    models
)


def get_examples(
    session: Session
) -> list[models.Example]:
    '''Get all examples'''
    query = session.query(models.Example).all()
    return query
