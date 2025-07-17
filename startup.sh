#! /bin/bash

#############################################################
################   UNTESTED   ###############################
#############################################################

# TODO: enable security features
generate secret key
echo "SECRET_KEY=$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')" >> .env

# static file preporation
python manage.py collectstatic || exit

# setup db scripts
python manage.py makemigrations || exit

# run db scrupts
python manage.py migrate || exit

#initialize starting data
python manage.py seed_data || exit

# start project - dev mode
# python manage.py runserver 0.0.0.0:8000 || exit

# start project - prod mode
# gunicorn --bind 0.0.0.0:8000 --workers 1 my_docker_django_app.wsgi:application