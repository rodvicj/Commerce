#!/usr/bin/env bash

set -e

# RUN_MANAGE_P='poetry run python manage.py'

# echo 'Collecting static files...'
# $RUN_MANAGE_PY collectstatic --no-input

# echo 'Running migrations...'
# $RUN_MANAGE_PY migrate --no-input
#
echo 'checking directory structure...'
ls

echo 'which poetry'
which poetry

echo 'which python'
which python

# exec ls -a
exec poetry run python manage.py runserver -p 8000 -b 0.0.0.0
# exec poetry run daphne thenewboston.project.asgi:application -p 8000 -b 0.0.0.0
# poetry run python manage.py runserver -p 8000 -b 0.0.0.0
