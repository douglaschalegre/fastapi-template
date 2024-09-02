"""Genéricos para a criação de erros"""

from typing import Any
from fastapi import HTTPException


def build_response(status_code: int, schema: dict, description: str | None = None):
    """Creating dictionary responses"""
    return {
        str(status_code): {
            'description': description,
            'content': {'application/json': {'schema': schema}},
        }
    }


class GenericError(HTTPException):
    """A GenericError to handling application errors with a safe OpenAPI3 integration."""

    def __init__(
        self,
        status_code: int = 500,
        message: str = 'Internal server error',
        description: str | None = None,
    ):
        self.status_code = status_code
        self.message = message
        self.schema = {
            'type': 'object',
            'properties': {
                'message': {
                    'type': 'string',
                    'example': message,
                }
            },
        }
        self.response = build_response(status_code, self.schema, description)
        super().__init__(status_code, detail=message)


class InternalError(GenericError):
    """500: Unknown internal error server."""

    def __init__(self):
        super().__init__(status_code=500, message='Internal server error')
        self.status_code = 500
        self.message = 'Internal server error'
        self.schema = {
            'type': 'object',
            'properties': {
                'message': {
                    'type': 'string',
                    'example': self.message,
                },
                'detail': {'type': 'string', 'example': '<<traceback>>'},
            },
        }
        self.response = build_response(self.status_code, self.schema, 'Unexpected internal error.')


class ResourceNotFoundError(GenericError):
    """404: Some requested resource cannot be found."""

    def __init__(self, resource: str = '<<some-resource>>'):
        super().__init__(
            status_code=404,
            message=f'Some requested resource cannot be found. Resource: {resource}',
        )


class ResourceAlreadyExists(GenericError):
    """409: Some requested resource cannot be found."""

    def __init__(self, resource: str = '<<some-resource>>'):
        super().__init__(
            status_code=409,
            message=f'Conflict in the request because resource already exists. Resource: {resource}',
        )


class BadRequestError(GenericError):
    """400: Some requested resource cannot be found."""

    def __init__(self, resource: str = '<<some-resource>>'):
        super().__init__(status_code=400, message=f'Bad request. Resource: {resource}')


class ForbiddenRequestError(GenericError):
    """403: Some requested resource is Forbidden."""

    def __init__(self, resource: str = '<<some-resource>>'):
        super().__init__(
            status_code=403, message=f'Requested resource is Forbidden. Resource: {resource}'
        )


def group_errors(
    status_code: int, errors: list[GenericError], description: str | None = None
) -> dict[str | int, dict[str, Any]]:
    """Grouping errors into a oneOf in OpenAPI3."""

    def get_schema(err: GenericError):
        """Recuperar o schema do OpenAPI da exception."""
        if isinstance(err, GenericError):
            return err.schema

    return {
        status_code: {
            'description': description,
            'content': {'application/json': {'schema': {'oneOf': list(map(get_schema, errors))}}},
        }
    }
