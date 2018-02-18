from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from django.shortcuts import render
from core.models import *

from .serializers import *

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class ActivityList(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class ActivityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class TimeEntryViewSet(viewsets.ModelViewSet):
    queryset = TimeEntry.objects.all()
    serializer_class = TimeEntrySerializer

class TimeEntryList(generics.ListCreateAPIView):
    queryset = TimeEntry.objects.all()
    serializer_class = TimeEntrySerializer

class TimeEntryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TimeEntry.objects.all()
    serializer_class = TimeEntrySerializer
