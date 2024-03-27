'''Generic consumer package to handle requests with token and exceptions'''
import json
from requests import request as raw_request


def request(token: str, **kwargs) -> dict:
    """Requests request with interceptors to handle token and commons exceptions."""

    headers: dict = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    if 'headers' in kwargs:
        headers.update(kwargs['headers'])
        del kwargs['headers']

    if 'data' in kwargs:
        kwargs['data'] = json.dumps(kwargs['data'])

    if 'params' in kwargs and kwargs['params'] is not None:
        for key, value in kwargs['params'].items():
            if isinstance(value, bool):
                kwargs['params'][key] = 'true' if value is True else 'false'

    if 'files' in kwargs:
        del headers['Content-Type']

    res = raw_request(headers=headers, **kwargs, timeout=100)

    return res.json()
