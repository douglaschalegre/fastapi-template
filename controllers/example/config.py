"""Tags description to Example API"""
from fastapi import APIRouter

EXAMPLE = dict(
    name='Example',
    description='API to manage examples.'
)

tags = [
    EXAMPLE,
]

router = APIRouter()
