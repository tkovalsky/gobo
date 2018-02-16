import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Contact(models.Model):
    name = models.CharField(blank=False, max_length=200)
    email = models.EmailField(primary_key=True, unique=True, blank=False, max_length=200)
    signup_type = models.CharField(max_length=1)
    message = models.TextField(blank=False, max_length=200)
    robot = models.BooleanField("not a robot", blank=False, default=False)

    def __str__(self):
        return self.email
