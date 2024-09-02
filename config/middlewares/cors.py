"""Cors config"""

cors = dict(
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
    expose_headers=['Authorization', 'authorization', 'Content-Type'],
)
