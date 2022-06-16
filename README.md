# Quenten

## Introduction

A survey application for Nottinghamshire Healthcare NHS Foundation Trust.

## Local Development

### With Python

`Python 3.10^` is required.

Install [Poetry](https://python-poetry.org/docs/).

1. In root directory, run `poetry install`
2. Enter virtual env, run `poetry shell`
3. CD to `/quenten/`
4. Run database migrations `python manage.py migrate`
5. Add a new user `python manage.py createsuperuser`
6. Run application `python manage.py runserver`
7. Open `http://localhost:8000/`

### Quickstart in Docker (todo)

Requires `docker`

1. Run `docker-compose up`
2. Open `http://localhost:8000/`
