from django.shortcuts import render
from .models import Job

from django.views.generic import FormView
from .forms import S3DirectUploadForm
# Create your views here.

def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})

def services(request):
    return render(request, 'jobs/services.html')

def contact(request):
    return render(request, 'jobs/contact.html')

def test(request):
    return render(request, 'jobs/test.html')

class MyView(FormView):
    template_name = 'form.html'
    form_class = S3DirectUploadForm
