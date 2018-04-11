from django.shortcuts import render

from airtable import Airtable

# Create your views here.
AT = Airtable('app722UkuB0eVMwVk',
              'Jobs',
              api_key='keyoOFryShWQQ1qGs')


def allwork(request):
    jobs = AT.get_all()
    return render(request, 'work/allwork.html', {'jobs':jobs})
