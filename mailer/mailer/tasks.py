# coding=utf-8
from datetime import datetime

from celery_tasks import app
from service import send
from models import Subscriber
from django.core.mail import send_mail
from django.template.loader import render_to_string


@app.task
def send_spam_email(data):
    send(data)


@app.task
def send_beat_email():
    # emails = []
    # for subscriber in Subscriber.objects.all():
    #     emails.append(subscriber.email)
    # #
    # print emails
    # send_mail(
    #     subject='Рассылка',
    #     message='Вы подписались на рассылку\nМы будем присылать вам много спама.'
    #             'Чтобы не расслаблялись',
    #     recipient_list=emails,
    #     from_email='hakuforprog@mail.ru',
    #     fail_silently=False
    # )
    for subscriber in Subscriber.objects.all():
        birthday = subscriber.birthday
        now = datetime.now().date()
        years_old = (now - birthday).days / 365
        data = {
            'name': subscriber.name,
            'email': subscriber.email,
            'years': years_old
        }
        template = render_to_string('mailer/mails/start_mail.html', context=data)
        send_mail(
            subject='Рассылка',
            message='',
            recipient_list=[subscriber.email],
            from_email='hakuforprog@mail.ru',
            html_message=template,
            fail_silently=False
        )
