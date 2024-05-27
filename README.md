# A starter for your next Django web app


![Static Badge](https://img.shields.io/badge/Django-%23092E20?style=for-the-badge&logo=django&logoColor=white)
![Static Badge](https://img.shields.io/badge/Poetry-%2360A5FA?style=for-the-badge&logo=poetry&logoColor=white)
![Static Badge](https://img.shields.io/badge/Docker-%232496ED?style=for-the-badge&logo=docker&logoColor=white)
![Static Badge](https://img.shields.io/badge/PostgreSQL-%234169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Static Badge](https://img.shields.io/badge/Celery-%2337814A?style=for-the-badge&logo=celery&logoColor=white)
![Static Badge](https://img.shields.io/badge/Redis-%23DC382D?style=for-the-badge&logo=redis&logoColor=white)
![Static Badge](https://img.shields.io/badge/Tailwind%20CSS-%2306B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)
![Static Badge](https://img.shields.io/badge/Htmx-%233366CC?style=for-the-badge&logo=htmx&logoColor=white)
![Static Badge](https://img.shields.io/badge/Material%20Design%20Icons-%232196F3?style=for-the-badge&logo=materialdesignicons&logoColor=white)


This is some boilerplate code, that I pieced together for my latest Django project.

Alongside a predefined development setup, you will find some helpful features to  get you started quickly for creating your next Django web application.

## Prerequisties

- Python 3.12
- PostgreSQL 16.2
- Docker 26.1
- Docker Compose 2.27


## Features

### Django
- Allauth
- Custom User Model
- Split settings
- context_processor
- Logger
- Poetry
- variables in .env.dev file (do not store your secrets in a public repository)

### Client
- Tailwind CSS with Flowbite
- HTMX
- Some templates with a predefined layout
- A landing page

### Convenience

Use the `Makefile` to shorten common and often used comands.

For example `poetry run python manage.py makemigrations` becomes `make mm`.

### Docker

Start your docker containers with `docker-compose -f docker-compose.dev.yaml up --build`.

Hook into your django container with `docker exec -it django_starter_web bash`.

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
