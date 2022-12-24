from django.forms import ModelForm

from apps.models import Url


class UrlForm(ModelForm):
    class Meta:
        model = Url
        exclude = ('short_name',)
