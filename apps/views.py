from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, TemplateView

from apps.forms import UrlForm
from apps.models import Url


# Create your views here.


class IndexFormView(FormView, TemplateView):
    form_class = UrlForm
    template_name = 'apps/index.html'
    success_url = reverse_lazy('main_view')

    def form_valid(self, form):
        url = form.save()
        url = f'{get_current_site(self.request)}/{url.short_name}'
        context = {
            'short_name': url,
        }
        return render(self.request, 'apps/index.html', context)


class ShortURlView(View):
    def get(self, request, name, *args, **kwargs):
        url = Url.objects.get(short_name=name)
        return HttpResponseRedirect(url.long_name)
