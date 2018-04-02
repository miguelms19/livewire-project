from django.shortcuts import render

from .models import Jobdetails
# Create your views here.

def home(request):
    jobs = Jobdetails.objects.all()
    return render(request, 'jobs/home.html', {'jobs':jobs})

def services(request):
    return render(request, 'jobs/services.html')
