#!/bin/sh

python manage.py makemigrations
python manage.py migrate
python manage.py open_weather_sync
python manage.py test
python manage.py runserver 0.0.0.0:8000