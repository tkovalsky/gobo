from django.contrib.auth.models import User
from core.models import *
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('name', 'description')


class TimeEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeEntry
        fields = ('activity', 'user', 'description', 'start', 'end')
