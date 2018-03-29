from django.contrib import admin

# Register your models here.
from .models import Jobdetails
from about.models import Team

admin.site.register(Jobdetails)
admin.site.register(Team)
