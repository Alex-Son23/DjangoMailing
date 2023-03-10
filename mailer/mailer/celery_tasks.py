import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mailer.settings')

app = Celery('mailer')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-spam-every-2-min': {
        'task': 'mailer.tasks.send_beat_email',
        'schedule': crontab(minute='*/2')
    }
}
