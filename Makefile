.PHONY: install
install:
	npm --prefix ./frontend/ install && poetry install

.PHONY: poetry-update
poetry-update:
	poetry update

.PHONY: poetry-shell
shell-shell:
	poetry shell

.PHONY: install-pre-commit
install-pre-commit:
	poetry run pre-commit uninstall; poetry run pre-commit install

.PHONY: lint
lint:
	poetry run pre-commit run --all-files

.PHONY: load-fixtures
load-fixtures:
	poetry run python -m commerce_core.manage loaddata fixtures

.PHONY: migrations
migrations:
	poetry run python -m commerce_core.manage makemigrations

.PHONY: migrate
migrate:
	poetry run python -m commerce_core.manage migrate

.PHONY: update
update: install migrate install-pre-commit ;

.PHONY: shell
shell:
	poetry run python -m commerce_core.manage shell

.PHONY: superuser
superuser:
	poetry run python -m commerce_core.manage createsuperuser

.PHONY: runserver
runserver:
	poetry run python -m commerce_core.manage runserver


# .PHONY: update-requirements
# update-requirements:
# 	poetry export --without-hashes --format=requirements.txt > requirements.txt





# .PHONY: install
# install:
# 	poetry install

# .PHONY: poetry-update
# poetry-update:
# 	poetry update

# .PHONY: makemigrations
# makemigrations:
# 	poetry run python manage.py makemigrations

# .PHONY: fixture
# fixture:
# 	poetry run python manage.py loaddata intial_data.json

# .PHONY: install-pre-commit
# install-pre-commit:
# 	poetry run pre-commit uninstall; poetry run pre-commit install

# .PHONY: lint
# lint:
# 	poetry run pre-commit run --all-files

# .PHONY: migrate
# migrate:
# 	poetry run python manage.py migrate

# .PHONY: shell
# shell:
# 	poetry run python manage.py shell


# .PHONY: superuser
# superuser:
# 	poetry run python manage.py createsuperuser

# .PHONY: export
# export:
# 	poetry export --without-hashes --format=requirements.txt > requirements.txt
