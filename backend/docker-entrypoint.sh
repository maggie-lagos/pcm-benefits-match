#!/bin/bash

set -e

# collect static files and apply db migrations
python manage.py collectstatic --noinput
python manage.py migrate

# start gunicorn server
gunicorn benefitsmatch.wsgi:application --bind 0.0.0.0:8000