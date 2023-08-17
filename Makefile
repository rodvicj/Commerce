.PHONY: install
install:
	poetry install

.PHONY: makemigrations
makemigrations:
	poetry run python manage.py makemigrations

.PHONY: migrate
migrate:
	poetry run python manage.py migrate

.PHONY: runserver
runserver:
	poetry run python manage.py runserver
