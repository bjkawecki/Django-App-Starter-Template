#!/bin/bash

set -e

RUN_MANAGE_PY="python manage.py"

# echo "Collecting static files..."
# $RUN_MANAGE_PY collectstatic --no-input

# echo "Running migrate..."
$RUN_MANAGE_PY migrate --fake-initial
$RUN_MANAGE_PY migrate

npm init -y
npm install tailwindcss postcss-cli autoprefixer

exec "$@"
