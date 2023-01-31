from django.views.generic.edit import CreateView

from forms import CreateSubscriberForm
from tasks import send_spam_email
from service import send
from models import Subscriber
from datetime import datetime


class AddSubscriber(CreateView):
    model = Subscriber
    form_class = CreateSubscriberForm
    success_url = '/'
    template_name = 'mailer/subscriber.html'

    def form_valid(self, form):
        form.save()
        print form.instance
        # birthday = datetime.strptime(form.instance.birthday, '%d.%m.%Y')
        birthday = form.instance.birthday
        now = datetime.now().date()
        years_old = (now-birthday).days / 365
        data = {
            'name': form.instance.name,
            'email': form.instance.email,
            'years': years_old
        }
        print send_spam_email.delay(data=data)
        return super(AddSubscriber, self).form_valid(form)

