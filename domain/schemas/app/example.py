'''Example schema'''
from domain.schemas.orm import (
    ExampleBase
)
from .child import Child


class Example(ExampleBase):
    '''Example schema'''
    childs: list[Child]
