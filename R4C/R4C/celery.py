import os

from celery import Celery

from R4C.settings import CELERY_BROKER_URL

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'R4C.settings')
app = Celery('R4C',
             broker=CELERY_BROKER_URL,
             include=['customers.tasks'])
