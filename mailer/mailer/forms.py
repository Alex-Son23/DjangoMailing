from django import forms

from models import Subscriber


class CreateSubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ('name', 'email', 'birthday')

    # def __init__(self, *args, **kwargs):
    #     super(CreateSubscriberForm, self).__init__(args, kwargs)
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs['class'] = 'form_control'
    #         field.help_text = ''
