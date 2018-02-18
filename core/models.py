import datetime
from django.conf import settings
from django.contrib.auth import get_user_model
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

class Activity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

class TimeEntry(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    start = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)
