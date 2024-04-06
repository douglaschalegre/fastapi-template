# pylint: disable=bare-except, broad-except
'''Middleware to redirect some endpoints (redirect_routes) APIs.'''
from starlette.datastructures import UploadFile
from requests import request as raw_request
from fastapi.responses import JSONResponse
from fastapi import Request, FastAPI
from ..server import base_url
from ..proxy import (
    BASE_PATH,
    REQUIRED_BASE_PATH_TO_REDIRECT,
    external_apis
)


async def from_starlette_to_requests(form):
    '''Function to convert a starlette Request formdata to requests formdata'''
    files = dict()
    for key in form:
        a_file: UploadFile = form[key]  # type:ignore
        filename = a_file.filename
        contents = await a_file.read()
        content_type = a_file.content_type
        files[key] = (filename, contents, content_type)
    return files


async def read_formdata(request: Request):
    '''Reading form-data'''
    try:
        form = await request.form()
        files = await from_starlette_to_requests(form)
    except Exception:
        files = None
    return files


async def read_json(request: Request):
    '''Reading form-data'''
    try:
        body = await request.json()
    except Exception:
        body = None
    return body


class RedirectToOtherApi:
    '''Middleware to redirect some routes to other APIs.'''

    def __init__(self, _app: FastAPI):

        self.base_path = BASE_PATH
        self.required_base_path = REQUIRED_BASE_PATH_TO_REDIRECT

        self.redirect_routes = {}

        for api in external_apis:
            route_key = api["redirecter"].replace(BASE_PATH, '')  # type:ignore
            self.redirect_routes[route_key] = dict(url=api["url"])

    type = "http"

    def is_redirectable(self, request: Request) -> None | dict:
        '''Check if request is redirectable to other API.'''

        url_without_base = request.url.path

        if base_url is not None and base_url != "":
            url_without_base = request.url.path.replace(base_url, '')

        has_base_path = url_without_base.startswith(self.base_path)

        if not has_base_path:
            if not self.required_base_path:
                route_key = url_without_base[1:url_without_base.find('/', 1)]
                if route_key in self.redirect_routes:
                    url_without_base = f'{self.base_path}{url_without_base}'
            else:
                return None

        current_path = url_without_base.replace(
            f'{self.base_path}', '', 1)

        current_route_key = current_path[:current_path.find('/', 1)]

        current_route = self.redirect_routes.get(current_route_key, None)

        if current_route is None:
            return None

        return dict(
            url=current_route['url'],
            path=current_path[current_path.find('/', 1):]
        )

    async def __call__(self, request: Request, call_next):

        redirectable = self.is_redirectable(request)

        if redirectable is not None:
            url = redirectable['url']
            path = redirectable['path']

            method = request.method
            query = request.url.query

            token = request.headers.get(
                "Authorization", "").replace('Bearer ', '')

            files = await read_formdata(request)
            body = await read_json(request)

            response = raw_request(
                method=method,
                url=f'{url}{path}?{query}',
                headers={
                    'Authorization': f'Bearer {token}'
                },
                files=files if files is not None else None,
                json=body if body is not None else None,
                timeout=300
            )

            if response.status_code == 200:
                return JSONResponse(
                    status_code=response.status_code,
                    content='' if response.text == '' else response.json())

        return await call_next(request)
