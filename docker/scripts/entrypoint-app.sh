#!/bin/sh

set -e

python manage.py migrate --no-input
python manage.py collectstatic --no-input
python manage.py test account.tests --no-input
uwsgi --ini /uwsgi.ini