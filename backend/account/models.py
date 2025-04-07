from django.contrib.auth.models import User
from django.db import models


class Account(User):
    lastname = models.CharField(max_length=48, default="Unknown")
    firstname = models.CharField(max_length=48, default="Unknown")
    patronymic = models.CharField(max_length=48, blank=True, default="Unknown")
