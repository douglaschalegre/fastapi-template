"""Exception handling middleware for the FastAPI application"""

import traceback
from typing import Union, Dict, Any

from fastapi.responses import JSONResponse
from fastapi import Request, HTTPException, FastAPI
from fastapi.exceptions import FastAPIError
from starlette.exceptions import HTTPException as StarletteHTTPException


def create_error_response(
    status_code: int, message: str, detail: Union[str, Dict[str, Any]] = None
) -> JSONResponse:
    """Create a standardized error response"""
    content = {'message': message}
    if detail:
        content['detail'] = detail
    return JSONResponse(status_code=status_code, content=content)


async def http_exception_handler(
    _req: Request, exc: Union[HTTPException, StarletteHTTPException]
) -> JSONResponse:
    """Exception handler for HTTP exceptions"""
    return create_error_response(
        status_code=exc.status_code,
        message=str(exc.detail),
    )


async def fastapi_error_handler(_req: Request, exc: FastAPIError) -> JSONResponse:
    """Exception handler for FastAPI specific errors"""
    return create_error_response(
        status_code=500,
        message='Internal server error',
        detail=str(exc),
    )


def register_exception_collector(app: FastAPI) -> None:
    """Register middleware to collect and handle exceptions."""

    app.add_exception_handler(StarletteHTTPException, http_exception_handler)
    app.add_exception_handler(HTTPException, http_exception_handler)
    app.add_exception_handler(FastAPIError, fastapi_error_handler)

    @app.middleware('http')
    async def exception_collector(request: Request, call_next) -> JSONResponse:
        """Middleware to collect and handle all exceptions"""
        try:
            response = await call_next(request)
            return response
        except (HTTPException, StarletteHTTPException) as http_err:
            # Let the registered exception handlers handle HTTP exceptions
            raise http_err
        except FastAPIError as fastapi_err:
            # Let the registered exception handler handle FastAPI errors
            raise fastapi_err
        except Exception as err:
            # Handle unexpected exceptions
            traceback.print_exc()
            return create_error_response(
                status_code=500,
                message='Internal server error',
                detail={
                    'error_type': err.__class__.__name__,
                    'error_message': str(err),
                    'traceback': traceback.format_exc(),
                },
            )
