from django.shortcuts import render, redirect
from .models import Event
from .utils import searchEvents
from .forms import EventForm
from django.contrib import messages

def blankPage(request):
    page = "blank"
    context = {'page':page}
    return render(request, 'events/blank.html',context)

def eventsPage(request):
    events, search_query = searchEvents(request)
    page = "events"
    context = {'page':page, 'events':events, 'search_query':search_query}
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

def addEvent(request):
    page = 'add-event'
    profile = request.user.profile
    form = EventForm()
    
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.owner = profile
            event.save()
            messages.success(request, 'Event added succefully!')
            return redirect('admin')

    context = {'page':page, 'form':form}
    return render(request, 'events/add-event.html', context)

def updateEvent(request, pk):
    page = 'update-event'
    profile = request.user.profile
    event = profile.event_set.get(id=pk)
    form = EventForm(instance=event)
    
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated succefully!')
            return redirect('admin')    

    context = {'page':page, 'form':form}
    return render(request, 'events/update-event.html', context)

def deleteEvent(request, pk):
    page = 'delete-event'
    event = Event.objects.get(id=pk)
    
    if request.method == 'POST':
        event.delete()
        messages.success(request, 'Event delete succefully!')
        return redirect('admin')    

    context = {'page':page, 'event':event}
    return render(request, 'events/delete-event.html', context)

def ticketPage(request):
    page = 'tickets'
    context = {'page':page}
    return render(request, 'events/tickets.html', context)