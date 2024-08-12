from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event
from django.views.generic import TemplateView

# Create your views here.

class HomePage(TemplateView):
    """
    Displays home page "
    """ 
    template_name = 'index.html'


class EventList(generic.EventView):
    model = Event