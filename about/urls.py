from django.urls import path

from . import views


urlpatterns = [
    path('', views.allteam, name='allteam'),

]
