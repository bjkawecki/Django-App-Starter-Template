#!/bin/bash

set -e

RUN_MANAGE_PY="python manage.py"

# echo "Collecting static files..."
# $RUN_MANAGE_PY collectstatic --no-input

#echo "Running makemigrations..."
#$RUN_MANAGE_PY makemigrations

# echo "Running migrate..."
# $RUN_MANAGE_PY migrate --fake users zero
# $RUN_MANAGE_PY migrate --no-input

exec "$@"
