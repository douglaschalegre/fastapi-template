"""Some general config for all controllers"""

from fastapi import APIRouter

LOGIN = dict(name='Login', description='API to manage login of users')
USER = dict(name='User', description='API to manage users.')

tags = [LOGIN, USER]

router = APIRouter()
