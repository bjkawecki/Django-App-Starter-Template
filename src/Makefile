.PHONY: i
i:
	poetry install

.PHONY: lint
lint:
	poetry run pre-commit run --all-files

.PHONY: mm
mm:
	poetry run python manage.py makemigrations

.PHONY: m
m:
	poetry run python manage.py migrate

.PHONY: run
run:
	poetry run python manage.py runserver

.PHONY: su
su:
	poetry run python manage.py makesuperuser

.PHONY: flake
flake:
	poetry run flake8
