from django.contrib import admin
from django.urls import path, include

from apps.views import IndexFormView, ShortURlView

urlpatterns = [
    path('', IndexFormView.as_view(), name='index_view'),
    path('<str:name>', ShortURlView.as_view(), name='short_view')
]
