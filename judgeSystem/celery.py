from __future__ import absolute_import

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'judgeSystem.settings')

from django.conf import settings

app = Celery('tasks')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.update(
    CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend',
    BROKER_URL = 'django://',
    CELERY_TASK_RESULT_EXPIRES=3600,
)
