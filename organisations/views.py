from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_list_or_404, render, redirect
from django.views.decorators.http import require_POST
from django.views.generic import ListView
from organisations.models import Event
from django.views import generic

# Create your views here.

class EventList(generic.ListView):
    queryset = Event.objects.all()
    template_name = "event_list.html"