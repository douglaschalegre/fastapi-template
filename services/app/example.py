'''Service layer for example module'''
from sqlalchemy.orm import Session

from domain import (
    models
)
from repositories.app import (
    example as example_repository
)


def get_examples(
    session: Session
) -> list[models.Example]:
    '''Get all examples'''
    return example_repository.get_examples(
        session=session
    )
