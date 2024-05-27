# A starter for your next Django web app


![Static Badge](https://img.shields.io/badge/Django-%23092E20?style=flat&logo=django&logoColor=%23092E20&labelColor=white)
![Static Badge](https://img.shields.io/badge/Docker-%232496ED?style=flat&logo=docker&logoColor=%232496ED&labelColor=white)
![Static Badge](https://img.shields.io/badge/Poetry-%2360A5FA?style=flat&logo=poetry&logoColor=%2360A5FA&labelColor=white)
![Static Badge](https://img.shields.io/badge/Htmx-%233366CC?style=flat&logo=htmx&logoColor=%233366CC&labelColor=white)
![Static Badge](https://img.shields.io/badge/Tailwind-%2306B6D4?style=flat&logo=tailwindcss&logoColor=%2306B6D4&labelColor=white)
![Static Badge](https://img.shields.io/badge/Material%20Design%20Icons-%232196F3?style=flat&logo=materialdesignicons&logoColor=%232196F3&labelColor=white)
![Static Badge](https://img.shields.io/badge/Celery-%2337814A?style=flat&logo=celery&logoColor=%2337814A&labelColor=white)
![Static Badge](https://img.shields.io/badge/Redis-%23DC382D?style=flat&logo=redis&logoColor=%23DC382D&labelColor=white)


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
