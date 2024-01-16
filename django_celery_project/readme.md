celery -A django_celery_project.celery worker --pool=solo -l info
python manage.py runserver