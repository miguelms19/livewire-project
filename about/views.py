from django.shortcuts import render
from django.http import HttpResponse
#from airtable import Airtable

from .models import Team
# Create your views here.
#AT = Airtable('app722UkuB0eVMwVk',
#              'Team',
#              api_key='keyoOFryShWQQ1qGs')

def allteam(request):
#    members = AT.get_all()
    #return render(request, 'about/about.html', {'members':members})
    return render(request, 'about/about.html')
