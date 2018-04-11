from django.shortcuts import render
from airtable import Airtable

AT = Airtable('app722UkuB0eVMwVk',
              'Jobs',
              api_key='keyoOFryShWQQ1qGs')

# Create your views here.

def home(request):
    jobs = AT.get_all()
    return render(request, 'jobs/home.html', {'jobs': jobs})

def services(request):
    return render(request, 'jobs/services.html')

def contact(request):
    return render(request, 'jobs/contact.html')
