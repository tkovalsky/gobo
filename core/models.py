import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text



class Contact(models.Model):
    name = models.CharField(blank=False, max_length=200)
    email = models.EmailField(primary_key=True, unique=True, blank=False, max_length=200)
    signup_type = models.CharField(max_length=1)
    message = models.TextField(blank=False, max_length=200)
    robot = models.BooleanField(blank=False, default=False)

    def __str__(self):
        return self.email
