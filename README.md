- Main frameworks and packages:
  - [FastAPI](https://fastapi.tiangolo.com/)
  - [SQLAlchemy](https://www.sqlalchemy.org/) ([PostgreSQL](https://www.postgresql.org/) database).

## Install Python

Install [Python](https://www.python.org/downloads/) (version 3.10).

## Set and activate virtual environment

In project folder, execute the following commands:

```bash
pip install pipenv
export PIPENV_VENV_IN_PROJECT="enabled"
mkdir .venv
pipenv shell
source .venv/Scripts/activate
```

## Set environment variables

Create a .env file with the required environment variables see [.env.example]

## Install required dependencies

Run the following installation command:

```bash
pipenv install --dev
```

## Run server

On virtual environment, execute

```bash
pipenv run start
```

## Documentation

While running the server, one can access the [API documentation](http://localhost:1337/docs).
