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

#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    context = {'latest_question_list': latest_question_list}
#    return render(request, 'core/index.html', context)

#def detail(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'core/detail.html', {'question': question})

#def results(request, question_id):
#    response = "You're looking at the results of question %s."
#    return HttpResponse(response % question_id)

#def vote(request, question_id):
#    return HttpResponse("You're voting on question %s." % question_id)
