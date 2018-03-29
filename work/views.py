from django.shortcuts import render

from jobs.models import Jobdetails
# Create your views here.

def allwork(request):
    jobs = Jobdetails.objects
    return render(request, 'work/allwork.html', {'jobs':jobs})
