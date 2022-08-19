#!/bin/bash
#TODO: hide sensitive data
cd /app
python manage.py migrate --noinput
echo "from django.contrib.auth.models import User; User.objects.create_superuser('ruha', 'ruha@goodgenius.com', 'password')" | python manage.py shell
python manage.py runserver 0.0.0.0:8000