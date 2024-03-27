'''Config to add on FastAPI generated schema a old API (Node.js)'''
import pathlib
from fastapi.openapi.utils import get_openapi

from fastapi import FastAPI
from requests import request
from .proxy import external_apis
current_dir = pathlib.Path(__file__).parent.resolve()


def put_redirecter(paths: dict, api: dict):
    '''Put a route redirecter router to node paths.'''
    new_paths = dict()

    if 'include' in api:
        for required_path in api['include']:
            if required_path['path'] in paths:
                path = paths.get(required_path['path'])
                if path is not None and required_path['method'] in path:
                    new_paths = {
                        **new_paths,
                        f'{api["redirecter"]}{required_path["path"]}': {
                            f'{required_path["method"]}': {
                                **path.get(required_path['method']),
                                'tags': [f'[PROXY] {api["name"]}']
                            }
                        }
                    }

    return new_paths


def append_components(openapi_schema, docs):
    '''Appending components to OpenAPI'''
    for component_item in ['responses', 'schemas']:
        openapi_schema['components'][component_item] = {
            **docs['components'].get(component_item, dict()),
            **openapi_schema['components'].get(component_item, dict()),
        }


def append_paths(openapi_schema, docs, api):
    '''Appending paths to OpenAPI'''
    openapi_schema['paths'] = {
        **put_redirecter(docs['paths'], api=api),
        **openapi_schema['paths'],
    }


def extend_openapi(app: FastAPI, base_url: str, tags: list):
    '''Function to extend OpenAPI with others OpenAPI.'''
    def builder():
        '''Callback to fast api'''
        servers = None
        if base_url is not None and base_url != "":
            servers = [{"url": base_url}]

        openapi_schema = get_openapi(
            title=app.title,
            version=app.version,
            description=app.description,
            servers=servers,
            routes=app.routes,
            tags=tags
        )

        for api in external_apis:
            if api["open_api_path"] is not None:
                raw_docs = request(
                    method='GET',
                    url=f'{api["url"]}{api["open_api_path"]}',
                    timeout=300
                )
                if raw_docs.status_code == 200:
                    docs = raw_docs.json()
                    append_components(openapi_schema, docs)
                    append_paths(openapi_schema, docs, api)

                    openapi_schema['tags'] = openapi_schema.get(
                        'tags', []) + [dict(
                            name=f'[PROXY] {api["name"]}',
                            description=api["description"]
                        )]

                else:
                    print(
                        f'Error when get OpenAPI from {api["name"]} with url {api["url"]}')

        return openapi_schema

    return builder
