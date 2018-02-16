from django.contrib import messages
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.template import loader


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

def signup(request):
    form_class = SignupForm
    return render(request, 'contact.html', {
        'form': form_class
    })

def services(request):
    return render(request, 'services.html')
