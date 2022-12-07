# Tribe Hired Backend Test

This application is intended for tribehired's dev team for review.

## Native Development Requirements

This project requires the following dependencies, so first install them on your system using your preferred method.
- Python 3.10
- Pipenv
- PostgreSQL 14 or above

## Development Setup and Installation

Make sure you are in the root directory of the project, the one with `Pipfile` in it.

First, copy the `dev-example.env` file over to `.env`. This holds the environmental variables to configure the project. The provided `dev-example.env` file is for development use not production.

Create/activate a development environment py running `pipenv shell`. then install all the packages from the `Pipfile` with the `pipenv install` command. 

Then run all available migrations to setup your Database with:
- Windows `py manage.py migrate` or `python manage.py migrate`.
- Mac `python3 manage.py migrate`.

Finally start the development server by running `python3 manage.py runserver`. The development server will listen on `127.0.0.1:8000` by default.

##### Useful Resources

- [Django Rest Framework filter](https://django-filter.readthedocs.io/en/stable/guide/rest_framework.html)
- [Django annotation](https://docs.djangoproject.com/en/4.1/topics/db/aggregation/)