run-server:
	poetry run python manage.py runserver

migrate:
	poetry run python manage.py migrate

migrations:
	poetry run python manage.py makemigrations
