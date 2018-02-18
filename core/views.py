from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.template import loader
from rest_framework import viewsets

from .models import Contact
from .forms import ContactForm

# Create your views here.


def home(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'form was posted') #this is optional but good for the user
    context = {
        'form': form,   #here you are passing the variable "form" to the template so you can use it like "{{form.as_p}}"
        }
    return render(request, 'home.html', context)
    #return render(request, 'home.html')


def casestudies(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form,   #here you are passing the variable "form" to the template so you can use it like "{{form.as_p}}"
        }
    return render(request, 'casestudies.html', context)

    #return render(request, 'casestudies.html')


def casestudies1(request):
    return render(request, 'casestudies1.html')


def services(request):
    return render(request, 'services.html')

def strategy(request):
    return render(request, 'strategy.html')

def platform(request):
    return render(request, 'platform.html')

def learning(request):
    return render(request, 'learning.html')

def leadgen(request):
    return render(request, 'leadgen.html')
