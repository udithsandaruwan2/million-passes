from django.shortcuts import render, get_object_or_404, redirect
from events.models import Event, Ticket
from django.contrib.auth.decorators import login_required
from uuid import UUID
# views.py (continued)
from django.http import HttpResponseNotFound
from events.models import TicketLevel
from django.contrib import messages
from .forms import OrderForm
from .models import Order

@login_required(login_url="login")
def checkoutPage(request, pk):
    page = 'checkout'
    event = get_object_or_404(Event, id=pk)
    ticket_levels = TicketLevel.objects.filter(event=pk)
    
    if request.method == 'POST':
        selected_option = request.POST.get('options')
        if selected_option is not None:
            return redirect('payment', selected_option)
        
        else:
            messages.success(request, 'Please select a ticket!')
    
    context = {'page': page, 'event': event, 'ticket_levels':ticket_levels}
    return render(request, 'checkouts/checkout-page.html', context)


@login_required(login_url="login")
def multiCheckoutPage(request, pk):
    page = 'checkout'
    event = get_object_or_404(Event, id=pk)
    ticket_levels = TicketLevel.objects.filter(event=pk)
    
    if request.method == 'POST':
        selected_option = request.POST.get('options')
        if selected_option is not None:
            return redirect('payment', selected_option)
        
        else:
            messages.success(request, 'Please select at least one ticket!')
    
    context = {'page': page, 'event': event, 'ticket_levels':ticket_levels}
    return render(request, 'checkouts/multi-checkout-page.html', context)




@login_required(login_url="login")
def paymentPage(request, pk):
    page = 'payment'
    profile = request.user.profile
    ticket_level = TicketLevel.objects.get(id=pk)
    form = OrderForm()
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.owner = profile 
            order.ticket_level = ticket_level
            order.stripe_payment_token = 'sample_token'
            order.save()
            return redirect('order-success-massage', order)
            
    ticket = get_object_or_404(TicketLevel, id=pk)
    event = ticket.event
    context = {'page': page, 'event': event, 'ticket':ticket, 'form':form}
    return render(request, 'checkouts/payment.html', context)

def orderSuccessPage(request, pk):
    page = 'order-success'
    order = Order.objects.get(id=pk)
    context = {'order':order}
    return render(request, 'checkouts/order-success.html', context)


