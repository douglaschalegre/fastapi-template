'''Middleware de preparação básica com a API de usuários da squid'''
import traceback
from fastapi.responses import JSONResponse
from fastapi import Request, HTTPException, FastAPI
from starlette.exceptions import HTTPException as StarletteHTTPException


async def http_exception_handler(_req, exc) -> JSONResponse:
    '''Exception handler to convert it as a JSON Response.'''
    return JSONResponse(
        status_code=exc.status_code,
        content=dict(
            message=exc.detail,
        )
    )


class ExceptionCollector:
    '''Middleware to collect and handle exceptions from Exception to JSON Response.'''

    def __init__(self, app: FastAPI):
        app.add_exception_handler(
            StarletteHTTPException, http_exception_handler)

    type = "http"

    async def __call__(self, request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except Exception as err:
            if isinstance(err, HTTPException):
                return JSONResponse(status_code=err.status_code, content=dict(message=err.detail))
            traceback.print_exc()
            detail = traceback.format_exc()
            return JSONResponse(status_code=500,
                                content=dict(message="Internal server error", detail=detail))
