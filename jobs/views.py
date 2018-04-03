from django.shortcuts import render

from .models import Job
# Create your views here.

def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})

def services(request):
    return render(request, 'jobs/services.html')

def contact(request):
    return render(request, 'jobs/contact.html')
