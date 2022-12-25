from django.forms import ModelForm

from apps.models import Url, Message


class UrlForm(ModelForm):
    class Meta:
        model = Url
        exclude = ('short_name',)


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ('author', 'email', 'message')
