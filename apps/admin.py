from django.contrib import admin

from apps.models import Message, Url


# Register your models here.

@admin.register(Message)
class OriginAdmin(admin.ModelAdmin):
    list_display = ('author', 'email', 'message')


@admin.register(Url)
class OriginAdmin(admin.ModelAdmin):
    list_display = ('long_name', 'short_name')
