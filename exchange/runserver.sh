#!/bin/bash
cd /app
python manage.py migrate --noinput
python manage.py runserver 0.0.0.0:8001