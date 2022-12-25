from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, TemplateView, CreateView

from apps import forms
from apps.forms import UrlForm, MessageForm
from apps.models import Url


# Create your views here.


class IndexFormView(FormView):
    form_class = UrlForm
    template_name = 'apps/index.html'
    success_url = reverse_lazy('main_view')

    def post(self, request, *args, **kwargs):
        if 'get_url' in request.POST:
            url_form = forms.UrlForm(request.POST)
            if url_form.is_valid():
                url = Url.objects.filter(long_name=url_form.data.get('long_name')).first()
                if not url:
                    url = url_form.save()
                url = f'{get_current_site(self.request)}/{url.short_name}'
                context = {
                    'short_name': url,
                }
                return render(self.request, 'apps/index.html', context)
        if 'send_message' in request.POST:
            message_form = forms.MessageForm(request.POST)
            if message_form.is_valid():
                message_form.save()
                return redirect('index_view')
        return super().post(request, *args, **kwargs)


class ShortURlView(View):
    def get(self, request, name, *args, **kwargs):
        url = Url.objects.get(short_name=name)
        return HttpResponseRedirect(url.long_name)
