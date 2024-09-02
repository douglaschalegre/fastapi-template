"""Middleware de preparação básica com a API de usuários da squid"""

import traceback
from fastapi.responses import JSONResponse
from fastapi import Request, HTTPException, FastAPI
from starlette.exceptions import HTTPException as StarletteHTTPException
from psqd_sdk.domain.exceptions import ConsumerException as SquidConsumerException
from sbwb_sdk.generics.exceptions import SbwbException


async def http_exception_handler(_req, exc) -> JSONResponse:
    """Exception handler to convert it as a JSON Response."""
    return JSONResponse(
        status_code=exc.status_code,
        content=dict(
            message=exc.detail,
        ),
    )


def register_exception_collector(app: FastAPI):
    """Register middleware to collect and handle exceptions."""

    app.add_exception_handler(StarletteHTTPException, http_exception_handler)

    @app.middleware('http')
    async def exception_collector(request: Request, call_next):
        """Middleware to collect and handle exceptions from Exception to JSON Response."""
        try:
            response = await call_next(request)
            return response
        except Exception as err:
            if isinstance(err, HTTPException):
                return JSONResponse(status_code=err.status_code, content=dict(message=err.detail))
            if isinstance(err, SbwbException):
                return JSONResponse(
                    status_code=err.status_code,
                    content=dict(
                        message='An error occurred in a SubWEB resource consumption.',
                        detail=err.message,
                    ),
                )
            if isinstance(err, SquidConsumerException):
                return JSONResponse(
                    status_code=err.status_code,
                    content=dict(
                        message='An error occurred in a Squid resource consumption.',
                        detail=err.message,
                    ),
                )
            traceback.print_exc()
            detail = traceback.format_exc()
            return JSONResponse(
                status_code=500,
                content=dict(message='Internal server error', detail=detail),
            )
