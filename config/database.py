"""Database config package"""

import os
from typing import Any
from sqlalchemy import create_engine, URL, util
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

from .env import application


load_dotenv()

# Environment variables might change depending on the chosen database.
# Make sure to setup your .env file accordingly.
# You might need to change the declarative_base on domain/models/generic.py

db: dict[str, Any] = dict(
    user=os.getenv('USER_DB'),
    password=os.getenv('PASS_DB'),
    host=os.getenv('HOST_DB'),
    port=os.getenv('PORT_DB') or 5432,
    schema=os.getenv('SCHEMA_DB') or 'postgres',
    name=os.getenv('NAME_DB'),
)


def build_db_url(params: dict[str, Any]) -> URL:
    """build db url"""
    return URL(
        drivername='postgresql',
        username=params['user'],
        password=params['password'],
        database=params['name'],
        host=params['host'],
        port=params['port'],
        query=util.immutabledict(dict(application_name=application['id'])),
    )


db['url'] = build_db_url(db)

engine = create_engine(db['url'], pool_size=5, echo=False, pool_pre_ping=True)
Session = sessionmaker(bind=engine, autocommit=False)


def get_session():
    """Função para geração da session."""
    session = Session()
    try:
        yield session
    except Exception:  # pylint: disable=broad-except
        session.rollback()
        raise
    else:
        session.commit()
    finally:
        session.close()
