.PHONY: install
install:
	poetry install

.PHONY: install-pre-commit
install-pre-commit:
	poetry run pre-commit uninstall; poetry run pre-commit install

.PHONY: lint
lint:
	poetry run pre-commit run --all-files

.PHONY: makemigrations
makemigrations:
	poetry run python manage.py makemigrations

.PHONY: migrate
migrate:
	poetry run python manage.py migrate

.PHONY: runserver
runserver:
	poetry run python manage.py runserver

.PHONY: superuser
superuser:
	poetry run python manage.py makesuperuser

.PHONY: update
update:
	install migrate install-pre-commit;

.PHONY: flake
flake:
	poetry run flake8

.PHONY: up-dependencies-only
up-dependencies-only:
	test -f .env || touch .env; docker-compose -f docker-compose.yaml up --force-recreate db
