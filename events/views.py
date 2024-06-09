from django.shortcuts import render
from .models import Event
from .utils import searchEvents
from django.utils import timezone
from datetime import timedelta

def blankPage(request):
    page = "blank"
    context = {'page':page}
    return render(request, 'events/blank.html',context)

def eventsPage(request):
    events, search_query = searchEvents(request)
    page = "events"
    context = {'page':page, 'events':events, 'search_query':search_query,}
    return render(request, 'events/events.html',context)

def aboutPage(request):
    page = "about"
    context = {'page':page}
    return render(request, 'events/about.html', context)

def singleEvent(request, pk):
    page = "single-event"
    event = Event.objects.get(id=pk)
    ticket_prices = event.ticket_prices.all()
    context = {'page':page, 'event':event, 'ticket_prices':ticket_prices}
    return render(request, 'events/single-event.html', context)
