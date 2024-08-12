from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Event


# Create your views here.

class HomePage(TemplateView):
    """
    Displays home page "
    """ 
    template_name = 'index.html'


class EventList(generic.EventView):
    model = Event