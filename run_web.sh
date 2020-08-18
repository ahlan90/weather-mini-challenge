#!/bin/sh

python manage.py makemigrations
python manage.py migrate
python manage.py read_csv_file
python manage.py test
python manage.py runserver 0.0.0.0:8000