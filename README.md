# A starter for your next Django web app


![Static Badge](https://img.shields.io/badge/Django-%23092E20?style=flat-square&logo=django&logoColor=white)
![Static Badge](https://img.shields.io/badge/Docker-%232496ED?style=flat-square&logo=docker&logoColor=white)
![Static Badge](https://img.shields.io/badge/Poetry-%2360A5FA?style=flat-square&logo=poetry&logoColor=white)
![Static Badge](https://img.shields.io/badge/Htmx-%233366CC?style=flat-square&logo=htmx&logoColor=white)
![Static Badge](https://img.shields.io/badge/Tailwind-%2306B6D4?style=flat-square&logo=tailwindcss&logoColor=white)
![Static Badge](https://img.shields.io/badge/Material%20Design%20Icons-%232196F3?style=flat-square&logo=materialdesignicons&logoColor=white)
![Static Badge](https://img.shields.io/badge/Celery-%2337814A?style=flat-square&logo=celery&logoColor=white)
![Static Badge](https://img.shields.io/badge/Redis-%23DC382D?style=flat-square&logo=redis&logoColor=white)


Boilerplate code to get you quickly started for the development of a Django web application.

## Features

### Convenience

Use the `Makefile` to shorten common and often used comands.

For example `poetry run python manage.py makemigrations` becomes `make mm`.

### Docker

- docker-compose -f docker-compose.dev.yaml build
- docker-compose -f docker-compose.dev.yaml up
- docker exec -it django_starter_web bash

### Lint
You can lint your files with pre-commit `poetry run pre-commit run --all-files`.
First time will install the hooks from .pre-compose-config.yaml.
Shortcut in Makefile: `make lint`

If you want to use `pre-commit` with `git`, you need to activate a virtual environment.

First, create the virtual environment. On GNU/Linux you do this by

`python -m venv .venv`

and activate it by

`source .venv/bin/activate`

In the first run, pre-commit will update your projects files according to your configuration.

For your django-templates files you can use djlint with `djlint . --reformat`

## Development
- Lint
- Makefile
- Poetry (dependencies and dev-dependencies)
- env files




## Django Quick Start
### Server
- Allauth
- Custom User Model
- Split settings
- context_processor
- Logger

### Client
- Templates
- Layout
- Landing Page
