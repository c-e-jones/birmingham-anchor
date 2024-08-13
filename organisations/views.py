from django.shortcuts import render
from django.views import generic
from .models import Event

# Create your views here.

class EventList(generic.ListView):
    model = Event

def frontpage(request):
    events = Event.objects.all
    
    return render(request, 'core/event_list.html')