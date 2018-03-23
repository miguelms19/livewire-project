from django.shortcuts import render

from about.models import Team
# Create your views here.

def allteam(request):
    member = Team.objects
    return render(request, 'about/about.html', {'member':member})
