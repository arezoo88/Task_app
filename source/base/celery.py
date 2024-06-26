
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings')

app = Celery('base')

# Using a string here means the worker will not have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')


app.conf.beat_schedule = {
    'send-task-reminders-every-hour': {
        'task': 'apps.project.tasks.send_task_reminders',
        'schedule': crontab(minute=0, hour='*'),
    },
    'send-daily-project-summary': {
        'task': 'apps.project.send_daily_project_summary',
        'schedule': crontab(minute=0, hour=0),
    },
}

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
