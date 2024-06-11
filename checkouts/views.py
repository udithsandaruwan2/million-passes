from django.shortcuts import render, get_object_or_404
from events.models import Event
from json import dumps 
import json 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def checkoutPage(request, pk):
    page = 'checkout'
    total = None
    event = get_object_or_404(Event, id=pk)
    ticket_prices = event.ticket_prices.filter(event=event)
    if request.method == 'POST':
        data = json.loads(request.body)
        total = data['total']
        counter = data['counter']

        # Temporarily store the total in the session or database as per your requirement
        request.session[f'total_{counter}'] = total

        return JsonResponse({'status': 'success'})
    context = {'page':page, 'event':event, 'ticket_prices':ticket_prices, 'total':total}
    return render(request, 'checkouts/checkout-page.html', context)
