'''Controllers for the example module'''
from fastapi import Depends
from sqlalchemy.orm import Session
from config import get_session
from services.app import (
    example as example_service
)
from domain import (
    schemas,
    models
)
from .config import (
    EXAMPLE, router,
)


@router.get(
    path='/examples',
    summary='Get all examples',
    tags=[EXAMPLE['name']],
    response_model=list[schemas.Example]
)
def get_examples(
    session: Session = Depends(get_session)
) -> list[models.Example]:
    '''Get all examples'''
    return example_service.get_examples(
        session=session
    )
