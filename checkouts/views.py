from django.shortcuts import render, get_object_or_404, redirect
from .utils import filter_and_update_tickets
from events.models import Event, Ticket
from django.contrib.auth.decorators import login_required
from uuid import UUID
# views.py (continued)
from django.http import HttpResponseNotFound
from events.models import TicketLevel
from django.contrib import messages
from .forms import OrderForm
from .models import Order
from django.http import HttpResponse
from urllib.parse import urlencode
import json
import urllib.parse
from .utils import send_order_email


@login_required(login_url="login")
def checkoutPage(request, pk):
    page = 'checkout'
    event = get_object_or_404(Event, id=pk)
    ticket_levels = TicketLevel.objects.filter(event=pk)
    
    if request.method == 'POST':
        selected_option = request.POST.get('options')
        if selected_option is not None:
            ticket_level = get_object_or_404(TicketLevel, id=selected_option)
            available_tickets = Ticket.objects.filter(status=1, ticket_level=ticket_level).exists()
            if available_tickets:
                return redirect('payment', selected_option)
            else:
                messages.error(request, 'Out of stock')
        
        else:
            messages.success(request, 'Please select a ticket!')
    
    context = {'page': page, 'event': event, 'ticket_levels':ticket_levels}
    return render(request, 'checkouts/checkout-page.html', context)







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
            return redirect('payment-gateway', order.id)
            
    ticket = get_object_or_404(TicketLevel, id=pk)
    event = ticket.event
    context = {'page': page, 'event': event, 'ticket':ticket, 'form':form}
    return render(request, 'checkouts/payment.html', context)







def orderSuccessPage(request, pk):
    page = 'order-success'
    order = Order.objects.get(id=pk)
    context = {'page':page, 'order':order}
    return render(request, 'checkouts/order-success.html', context)

def multiOrderSuccessPage(request, pk):
    page = 'multi-order-success'
    decoded_orders = urllib.parse.unquote(pk)
    orders = json.loads(decoded_orders)
    
    qrs = []
    
    for order in orders:
        order_ = Order.objects.get(id=order)
        qrs.append(order_.qr_code)
    context = {'page':page, 'qrs':qrs}
    return render(request, 'checkouts/order-success.html', context)




# Assuming this is where your function is

def download_qr_codes(request):
    page = "bulk-download"
    profile = request.user.profile
    ticket_levels = TicketLevel.objects.filter(owner=profile)
    
    if request.method == 'POST':
        tl = request.POST.get('ticketLevel')
        qty = request.POST.get('quantity')
        
        if tl is not None:
            ticket_level = get_object_or_404(TicketLevel, id=tl)
            available_tickets = Ticket.objects.filter(status=1, ticket_level=ticket_level).exists()
            if available_tickets:
                try:
                    qty = int(qty)
                except ValueError:
                    return HttpResponse("Invalid quantity", status=400)
                
                zip_buffer = filter_and_update_tickets(qty, tl)
                
                if not zip_buffer:
                    return HttpResponse("No tickets available", status=404)

                response = HttpResponse(zip_buffer, content_type='application/zip')
                response['Content-Disposition'] = 'attachment; filename="qr_codes.zip"'
                return response
            else:
                messages.error(request, 'Out of stock')
        else:
                messages.error(request, 'Please select a ticket!')
        
        
    
    context = {'ticket_levels': ticket_levels, 'page':page}
    return render(request, 'checkouts/download-tickets.html', context)






@login_required(login_url="login")
def multiPaymentPage(request, pk):
    page = 'multi-payment'
    profile = request.user.profile
    form = OrderForm()
    event = get_object_or_404(Event, id=pk)

    orders = []

    total_price = None
    selected_tickets = None

    if request.method == 'GET':
        total_price = request.GET.get('total_price')
        selected_tickets = request.GET.get('selected_tickets')

    if request.method == 'POST':
        total_price = request.POST.get('total_price')
        selected_tickets = request.POST.get('selected_tickets')


        selected_tickets = json.loads(selected_tickets)



        total_price = float(total_price)


        form = OrderForm(request.POST)
        if form.is_valid():
            for ticket in selected_tickets:
                order = form.save(commit=False)
                order.owner = profile
                order.ticket_levels = ticket['ticket_name']
                order.stripe_payment_token = 'sample_token'
                order.save()
                orders.append(order.id)
                    
            serialized_orders = json.dumps(orders)
            encoded_orders = urllib.parse.quote(serialized_orders)
            return redirect('multi-order-success-message', pk=encoded_orders)

    context = {
        'page': page,
        'event': event,
        'form': form,
        'total_price': total_price,
        'selected_tickets': selected_tickets
    }
    return render(request, 'checkouts/payment.html', context)







from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.http import urlencode
from django.contrib.auth.decorators import login_required
import json

@login_required(login_url="login")
def multiCheckoutPage(request, pk):
    page = 'checkout'
    event = get_object_or_404(Event, id=pk)
    ticket_levels = TicketLevel.objects.filter(event=pk)

    if request.method == 'POST':
        selected_options = request.POST.getlist('options')

        for selected_option in selected_options:
            if selected_option is not None:
                ticket_level = get_object_or_404(TicketLevel, id=selected_option)
                available_tickets = Ticket.objects.filter(status=1, ticket_level=ticket_level).exists()
                if available_tickets:
                    total_price = 0
                    selected_tickets = []

                    for ticket_id in selected_options:
                        name = request.POST.get(f'name_{ticket_id}')
                        quantity = request.POST.get(f'quantity_{ticket_id}')
                        if quantity:
                            price = request.POST.get(f'price_{ticket_id}')
                            
                            if price is None:
                                # Handle the case where the price is not found, e.g., set a default value or raise an error
                                price = 0.0  # Default value, or you can handle it differently
                            else:
                                price = float(price)

                            total_price += price * int(quantity)
                            selected_tickets.append({'ticket_id': ticket_id, 'ticket_name':name, 'quantity': quantity, 'price': price})

                    # Serialize selected_tickets to JSON
                    selected_tickets_json = json.dumps(selected_tickets)

                    # Create query parameters
                    query_params = {
                        'total_price': total_price,
                        'selected_tickets': selected_tickets_json,
                    }
                    query_string = urlencode(query_params)

                    return redirect(f'{reverse("multi-payment", args=[pk])}?{query_string}')
                else:
                    messages.error(request, 'Out of stock')
            
            else:
                messages.error(request, 'Please select at least one ticket!')

        

    context = {'page': page, 'event': event, 'ticket_levels': ticket_levels}
    return render(request, 'checkouts/multi-checkout-page.html', context)


from django.shortcuts import render

def paymentGateway(request, pk):
    
    order = Order.objects.get(id=pk)
    
    if request.method == "POST":
        card_number = request.POST.get('number-input')  # Replace 'number-input' with the actual name of your input field
        card_number = str(card_number)
        if card_number:
            if card_number == "0000-0000-0000-0000":
                send_order_email(order)
                return redirect('order-success-massage', order)

        
        # Add your payment processing logic here

    return render(request, 'checkouts/payment-gateway.html')
