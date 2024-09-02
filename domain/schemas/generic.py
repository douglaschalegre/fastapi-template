"""Generic classes and resources for schema building."""

from pydantic import BaseModel, ConfigDict

from utils.camel import to_camel


class GenericSchema(BaseModel):
    """Generic Class for schemas."""

    model_config = ConfigDict(
        alias_generator=to_camel,  # type: ignore
        populate_by_name=True,
    )


class TableSchema(GenericSchema):
    """Class for schemas based on database table.."""

    model_config = ConfigDict(from_attributes=True)
