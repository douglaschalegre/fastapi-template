"""Importing server env variables"""

import os
from dotenv import load_dotenv

load_dotenv()

base_url = os.getenv('SUB_DIR') or ''
port = int(os.getenv('SERVER_PORT') or '1337')
