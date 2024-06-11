from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, TicketPrices
from .utils import searchEvents
from .forms import EventForm, TicketForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def blankPage(request):
    page = "blank"
    context = {'page': page}
    return render(request, 'events/blank.html', context)

def eventsPage(request):
    events, search_query = searchEvents(request)
    page = "events"
    context = {'page': page, 'events': events, 'search_query': search_query}
    return render(request, 'events/events.html', context)

def aboutPage(request):
    page = "about"
    context = {'page': page}
    return render(request, 'events/about.html', context)

def singleEvent(request, pk):
    page = "single-event"
    event = get_object_or_404(Event, id=pk)
    ticket_prices = event.ticket_prices.filter(event=event)
    context = {'page': page, 'event': event, 'ticket_prices': ticket_prices}
    return render(request, 'events/single-event.html', context)

@login_required(login_url="login")
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
            messages.success(request, 'Event added successfully!')
            return redirect('admin')

    context = {'page': page, 'form': form}
    return render(request, 'events/add-event.html', context)

@login_required(login_url="login")
def updateEvent(request, pk):
    page = 'update-event'
    profile = request.user.profile
    event = get_object_or_404(profile.event_set, id=pk)
    form = EventForm(instance=event)
    
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated successfully!')
            return redirect('admin')

    context = {'page': page, 'form': form}
    return render(request, 'events/update-event.html', context)

@login_required(login_url="login")
def deleteEvent(request, pk):
    page = 'delete-event'
    event = get_object_or_404(Event, id=pk)
    
    if request.method == 'POST':
        event.delete()
        messages.success(request, 'Event deleted successfully!')
        return redirect('admin')

    context = {'page': page, 'event': event}
    return render(request, 'events/delete-event.html', context)

@login_required(login_url="login")
def ticketPage(request):
    page = 'tickets'
    profile = request.user.profile
    tickets = TicketPrices.objects.filter(owner=profile)
    context = {'page': page, 'tickets': tickets}
    return render(request, 'events/tickets.html', context)

@login_required(login_url="login")
def addTicket(request):
    page = 'add-ticket'
    profile = request.user.profile
    form = TicketForm()
    
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.owner = profile
            ticket.save()
            messages.success(request, 'Ticket added successfully!')
            return redirect('tickets')

    context = {'page': page, 'form': form}
    return render(request, 'events/add-ticket.html', context)

# @login_required(login_url="login")
# def updateTicket(request, pk):
#     page = 'update-ticket'
#     profile = request.user.profile
#     ticket = get_object_or_404(TicketPrices, id=pk)
#     form = TicketForm(instance=ticket)
    
#     if request.method == 'POST':
#         form = TicketForm(request.POST, instance=ticket)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Ticket updated successfully!')
#             return redirect('tickets')

#     context = {'page': page, 'form': form}
#     return render(request, 'events/update-ticket.html', context)


@login_required(login_url="login")
def deleteTicket(request, pk):
    page = 'delete-ticket'
    ticket = get_object_or_404(TicketPrices, id=pk)
    
    if request.method == 'POST':
        ticket.delete()
        messages.success(request, 'Tickets deleted successfully!')
        return redirect('tickets')

    context = {'page': page, 'ticket': ticket}
    return render(request, 'events/delete-ticket.html', context)