from django.conf.urls import url
from django.urls import include, path
from django.contrib.auth.models import User
from django.contrib import admin
from rest_framework import routers, serializers, viewsets

from .views import *

from .serializers import *

# ViewSets define the view behavior.

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('/users', UserViewSet)
router.register('/activities', ActivityViewSet)
router.register('/time-entries', TimeEntryViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('/auth', include('rest_framework.urls', namespace='rest_framework'))
]
