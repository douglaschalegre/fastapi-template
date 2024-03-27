"""Creation of controller list"""

from .users import (
    USERS,
    router as users_router
)
from .auth import (
    AUTHENTICATION,
    router as auth_router
)
from . import health

from . import project
from . import project_type
from . import task
from . import revision
from . import artifact

routes = [
    auth_router,
    users_router,
    project_type.router,
    project.router,
    task.router,
    revision.router,
    artifact.router,
    health.router,
]

tags = [
    AUTHENTICATION,
    USERS,
    *project_type.tags,
    *project.tags,
    *task.tags,
    *revision.tags,
    *artifact.tags,
    *health.tags,
]
