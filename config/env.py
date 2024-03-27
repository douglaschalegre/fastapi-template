'''Env var importing package'''
import logging
import os
from dotenv import load_dotenv


load_dotenv()

environment = os.getenv('ENVIRONMENT') or 'dev'

application = dict(
    id=os.getenv('APP_ID') or 'fastapi-template',
    name=os.getenv('APP_NAME') or 'FastAPI Template',
)

debug_mode = False  # type: ignore
if os.getenv('DEBUG_MODE') is not None:
    debug_mode = os.getenv('DEBUG_MODE').upper() == "TRUE"  # type:ignore
    disable_debug_query = os.getenv('DISABLE_DEBUG_QUERY', "FALSE") == "TRUE"
    if debug_mode:
        logging.getLogger().setLevel(logging.INFO)
    if debug_mode and not disable_debug_query:
        logging.basicConfig()
        logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
