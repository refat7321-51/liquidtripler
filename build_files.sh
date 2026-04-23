#!/bin/bash
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate --noinput
python manage.py shell -c "from django.contrib.auth.models import User; [User.objects.create_superuser(u, f'{u}@ex.com', '730323') for u in ['admin_refat', 'admin_ridoy', 'admin_rafi'] if not User.objects.filter(username=u).exists()]"
