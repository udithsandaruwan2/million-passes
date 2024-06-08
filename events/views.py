from django.shortcuts import render
from .models import Event

def blankPage(request):
    page = "blank"
    context = {'page':page}
    return render(request, 'events/blank.html',context)

def eventsPage(request):
    events = Event.objects.all()
    page = "events"
    context = {'page':page, 'events':events}
    return render(request, 'events/events.html',context)

def aboutPage(request):
    page = "about"
    context = {'page':page}
    return render(request, 'events/about.html', context)

def singleEvent(request, pk):
    page = "single-event"
    context = {'page':page}
    return render(request, 'events/single-event.html', context)
