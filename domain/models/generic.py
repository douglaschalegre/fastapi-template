"""Informações genéricas para os modelos"""
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from config.database import db

metadata_obj = MetaData(schema=db["schema"])
Base = declarative_base(metadata=metadata_obj)

ALL_DELETE = 'all, delete'


class GenericBase(Base):
    """Base class to build schemas."""
    __abstract__ = True
