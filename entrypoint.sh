#!usr/bin/bash

python manage.py migrate

gunicorn \
    --bind 0.0.0.0:8080 \
    --workers 7 \
    --log-level=debug \
    --timeout 600 csa.wsgi:application
