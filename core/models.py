import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Contact(models.Model):
    name = models.CharField(blank=False, max_length=200)
    email = models.EmailField(primary_key=True, unique=True, blank=False, max_length=200)
    message = models.TextField(blank=False, max_length=200)
    not_a_robot = models.BooleanField(blank=False, default=False)

    def __str__(self):
        return self.email
