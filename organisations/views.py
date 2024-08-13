from django.shortcuts import render
from django.views import generic
from organisations.models import Event

# Create your views here.

class EventList(generic.ListView):
    model = Event

def frontpage(request):
    events = Event.objects.all
    context = {'events': events}
    return render(request, '/event_list.html', context)