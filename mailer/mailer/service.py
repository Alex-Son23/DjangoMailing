# coding=utf-8
from django.core.mail import send_mail
import sys
from django.template.loader import render_to_string

reload(sys)
sys.setdefaultencoding('utf-8')


def send(data):
    template = render_to_string('mailer/mails/start_mail.html', context=data)
    print type(template)
    # context = {'name': user_name}
    # print get_template_sources('mails/start_mail.html')
    send_mail(
        subject='Рассылка',
        # message='Вы подписались на рассылку\nМы будем присылать вам много спама.'.encode(encoding='UTF-8'),
        message='',
        recipient_list=[str(data['email'])],
        # recipient_list='hakuforprog@gmail.com',
        from_email='hakuforprog@mail.ru',
        # auth_user='hakuforprog@mail.ru',
        # auth_password='QN13HtvLSuaNPMyattyu',
        html_message=str(template),
        fail_silently=False
    )
