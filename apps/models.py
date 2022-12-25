from random import choice
from string import ascii_letters, digits

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField, BooleanField, EmailField, TextField


# Create your models here.

class Url(models.Model):
    short_name = CharField(max_length=255)
    long_name = CharField(max_length=255)

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if not self.short_name:
            self.short_name = self.get_unique_url()

        super().save(force_insert, force_update, using, update_fields)

    def __token(self):
        return ''.join((choice(ascii_letters + digits) for i in range(7)))

    def get_unique_url(self):
        short_name = self.__token()
        while Url.objects.filter(short_name=short_name).exists():
            short_name = self.__token()
        return short_name


class Message(models.Model):
    author = CharField(max_length=255)
    email = EmailField()
    message = TextField()
