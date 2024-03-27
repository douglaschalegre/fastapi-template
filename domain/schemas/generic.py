"""Generic classes and resources for schema building."""
from pydantic import BaseModel

from utils.camel import to_camel


class GenericSchema(BaseModel):
    """Generic Class for schemas."""
    class Config:
        """Schema config class"""
        alias_generator = to_camel
        allow_population_by_field_name = True


class TableSchema(GenericSchema):
    """Class for schemas based on database table.."""
    class Config:
        """Schema config class"""
        orm_mode = True
