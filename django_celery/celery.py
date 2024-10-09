# celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set the default Django settings module for the Celery program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery.settings')

app = Celery('django_celery')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
