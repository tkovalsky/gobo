"""gobo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.contrib import admin
from core import views


urlpatterns = [
    path('core/', include('core.urls')),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('studies/', views.studies, name='studies'),
    path('services/', views.services, name='services'),
    path('services/strategy', views.strategy, name='strategy'),
    path('services/platform', views.platform, name='platform'),
    path('services/learning', views.learning, name='learning'),
    path('services/leadgen', views.leadgen, name='leadgen'),

]
