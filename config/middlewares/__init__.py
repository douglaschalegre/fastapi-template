'''Criação de lista de middlewares'''
from .exception import ExceptionCollector
from .redirect import RedirectToOtherApi
from .cors import cors
from .log import log_request_middleware

middlewares = [
    ExceptionCollector,
    RedirectToOtherApi,
]
