'''Model for adjacent task'''
from uuid import uuid4
from sqlalchemy import Column, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import text
from config.database import db
from .generic import GenericBase


class Child(GenericBase):
    '''Child model'''
    __tablename__ = 'child'

    id = Column('chil_id', UUID(as_uuid=True),
                UUID(as_uuid=True), default=uuid4, primary_key=True)
    example_id = Column('exam_id', UUID(as_uuid=True),
                        ForeignKey(f'{db["schema"]}.example.exam_id'))
    created_at = Column('exam_created_at', DateTime,
                        server_default=text('NOW()'))

    parent = relationship(
        'Example',
        back_populates='childs'
    )
