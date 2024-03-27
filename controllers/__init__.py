"""Creation of controller list"""

from . import health
from . import example

routes = [
    example.router,

    health.router,  # health route must be the last one!
]
tags = [
    *example.tags,
    *health.tags,  # health tag must be the last one!
]
