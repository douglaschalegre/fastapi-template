from pathlib import Path
from fastapi import Request, FastAPI
from pyinstrument import Profiler
from pyinstrument.renderers.html import HTMLRenderer
from pyinstrument.renderers.speedscope import SpeedscopeRenderer
from config.env import enable_profiling

current_dir = Path(__file__).parent


def register_profiling_middleware(app: FastAPI):
    """Register middleware that profiles the current request."""
    if enable_profiling is True:

        @app.middleware('http')
        async def profile_request(request: Request, call_next):
            """Profile the current request

            Taken from https://pyinstrument.readthedocs.io/en/latest/guide.html#profile-a-web-request-in-fastapi
            with slight improvements.

            """
            profile_type_to_ext = {'html': 'html', 'speedscope': 'speedscope.json'}
            profile_type_to_renderer = {
                'html': HTMLRenderer,
                'speedscope': SpeedscopeRenderer,
            }
            if request.query_params.get('profile', False):
                profile_type = request.query_params.get('profile_format', 'speedscope')
                with Profiler(interval=0.001, async_mode='enabled') as profiler:
                    response = await call_next(request)
                extension = profile_type_to_ext[profile_type]
                renderer = profile_type_to_renderer[profile_type]()
                with open(current_dir / f'./profile.{extension}', 'w') as out:
                    out.write(profiler.output(renderer=renderer))
                return response
            return await call_next(request)
