from django import forms
from mailing.models import Mailing, Client, Message

frequency_choices = [
        ('daily', 'ежедневно'),
        ('weekly', 'еженедельно'),
        ('monthly', 'ежемесячно')
    ]

status_choices = [
        ("created", "Создана"),
        ("completed", "Завершена"),
        ("started", "Запущена"),
    ]

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != "is_active":
                field.widget.attrs['class'] = 'form-control'


class ClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        exclude = ('owner',)


class MailingForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Mailing
        exclude = ('owner',)


class MessageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Message
        exclude = ('client',)


