from django.contrib import admin

# Register your models here.
from .models import Job
from about.models import Team

admin.site.register(Job)
admin.site.register(Team)
