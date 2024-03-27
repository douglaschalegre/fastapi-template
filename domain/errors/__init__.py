"""Export all errors from this package."""

from .generic import (group_errors,
                      InternalError,
                      ResourceNotFoundError,
                      ResourceAlreadyExists,
                      BadRequestError,
                      ForbiddenRequestError,
                      )


base_errors = {
    **group_errors(400, [
        BadRequestError(),
    ]),
    **group_errors(401, [
    ]),
    **group_errors(403, [
        ForbiddenRequestError(),
    ]),
    **group_errors(404, [
        ResourceNotFoundError(),
    ]),
    **group_errors(409, [
        ResourceAlreadyExists(),
    ]),
    **group_errors(500, [
        InternalError(),
    ]),
}
