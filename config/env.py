"""Env var importing package"""

import logging
import os
from dotenv import load_dotenv


load_dotenv()

environment = os.getenv('ENVIRONMENT') or 'dev'

application = dict(
    id=os.getenv('APP_ID') or 'fastapi-template',
    name=os.getenv('APP_NAME') or 'FastAPI Template',
)

DEBUG_MODE = False  # type: ignore
if os.getenv('DEBUG_MODE') is not None:
    DEBUG_MODE = os.getenv('DEBUG_MODE').upper() == 'TRUE'  # type:ignore
    disable_debug_query = os.getenv('DISABLE_DEBUG_QUERY', 'FALSE') == 'TRUE'
    if DEBUG_MODE:
        logging.getLogger().setLevel(logging.INFO)
    if DEBUG_MODE and not disable_debug_query:
        logging.basicConfig()
        logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
