#!/usr/bin/env bash
set -o errexit

# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Recolectar estáticos
python manage.py collectstatic --no-input

# 3. Correr migraciones (esto ya lo tenías)
python manage.py migrate

# 4. Crear el superusuario de forma automática (LA NUEVA PARTE)
python manage.py shell -c "from django.contrib.auth import get_user_model; import os; User = get_user_model(); User.objects.filter(username=os.getenv('ADMIN_USER')).exists() or User.objects.create_superuser(os.getenv('ADMIN_USER'), os.getenv('ADMIN_EMAIL'), os.getenv('ADMIN_PASSWORD'))"