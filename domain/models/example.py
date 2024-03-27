'''Model for adjacent task'''
from uuid import uuid4
from sqlalchemy import Column, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import text
from .generic import GenericBase


class Example(GenericBase):
    '''Example model'''
    __tablename__ = 'example'

    id = Column('exam_id', UUID(as_uuid=True),
                default=uuid4, primary_key=True)
    created_at = Column('exam_created_at', DateTime,
                        server_default=text('NOW()'))

    childs = relationship(
        'ForeignKey',
        back_populates='parent'
    )
