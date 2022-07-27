# Quenten

## Introduction

A survey application for Nottinghamshire Healthcare NHS Foundation Trust.

## Local Development

### With Python

`Python 3.10^` is required.

Install [Poetry](https://python-poetry.org/docs/).

Your `.env` file should contain:

```text
SECRET_KEY=generatedkey
```

1. In root directory, run `poetry install`
2. Enter virtual env, run `poetry shell`
3. CD to `/quenten/`
4. Run database migrations `python manage.py migrate`
5. Add a new user `python manage.py createsuperuser`
6. Seed initial form values `python manage.py loaddata seed_data.json --app web`
7. Run application `python manage.py runserver`
8. Open `http://localhost:8000/`

## Overview

It is a straightforward Django application, allowing users to enter survey data and "code" their responses accordingly.

The application is in the `web` directory.

* `/web/models.py` handles the database classes.
* `/web/views.py` handles the user views.
* `/web/forms.py` handles the forms logic.

Dependencies:

* `django-crispy-forms` is used to build the forms explicitly.
* `django-filter` is used to enable filtering on list views.
* `django-model-utils` `InheritanceManager()` is used to manage the object queries, allowing access to object subclasses.

### How to change question responses

The initial question responses are seeded into the database through `/web/fixtures/seed_data.json`. You can then amend these values in the Django admin.

### How to add a new form

The application is built around the initial five forms, adding new forms should replicate this logic.

1. Add a new model in `web/models.py`, all the responses subclass the `Person` model.
2. Add any further fields to this model, or add the existing mixins as necessary (for example, the `DemographicsMixin`)
3. Make database migrations in `/quenten/`: `python manage.py makemigrations` and `python manage.py migrate`
4. Add new form in `web/forms.py`, all the responses subclass the `Person` form. You override `get_form_layout` to explicitly build your new form layout, see [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/layouts.html) documentation.
5. Add the new form choice to `PersonSelectForm`.
6. In `web/views.py` add the new form choice to `PersonSelectView` `PersonCreateView`, `PersonUpdateView`.
