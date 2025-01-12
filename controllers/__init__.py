"""Creation of controller list"""

from .config import router, tags
from . import health

from .login import *
from .user import *

routes = [
    router,
    health.router,  # health route must be the last one!
]
tags = [
    *tags,
    *health.tags,  # health tag must be the last one!
]
