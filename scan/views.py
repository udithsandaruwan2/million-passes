from django.shortcuts import get_object_or_404
from django.shortcuts import render
import urllib.parse
from .forms import QRCodeForm
from .models import QRCode
from pyzbar.pyzbar import decode
from PIL import Image

from PIL import Image
from pyzbar.pyzbar import decode

def scan_qr_code(image):
    try:
        # Open image using PIL (Python Imaging Library)
        pil_image = Image.open(image)
        
        # Decode QR code using pyzbar
        decoded_objects = decode(pil_image)
        
        # Extract data from the first QR code found (assuming only one QR code in the image)
        for obj in decoded_objects:
            return obj.data.decode('utf-8')
        
        # Return None if no QR code is found
        return None
    
    except Exception as e:
        print(f"Error scanning QR code: {str(e)}")
        return None


from django.http import HttpResponseServerError
from django.shortcuts import render
from .forms import QRCodeForm
from .models import QRCode
from events.models import Ticket


def scan_view(request):
    page = "scan"
    context = {'page':page}
    return render(request, 'scan/scan.html', context)

def failurePage(request):
    return render(request, 'scan/failure.html')




# views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import urllib.parse

# Import your QRCode model
from .models import QRCode

from django.shortcuts import render
from django.http import JsonResponse
import json
import urllib.parse
from .models import QRCode # Assuming QRCode and Ticket models are imported from your models.py

@csrf_exempt
def qr_code_handler(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            qr_data = data.get('data')
            decoded_data = urllib.parse.unquote(qr_data)

            # Split the decoded string by commas to get individual key-value pairs
            data_parts = decoded_data.split(', ')

            # Extract and strip the values from the key-value pairs
            ticket_id = data_parts[0].split(':')[1].strip()
            ticket_level = data_parts[1].split(':')[1].strip()
            event = data_parts[2].split(':')[1].strip()
            price = int(data_parts[3].split(':')[1].strip())

            # Assuming QRCode is a defined class with the appropriate attributes and save method
            qr_code = QRCode(
                ticket_id=ticket_id,
                ticket_level=ticket_level,
                event=event,
                price=price
            )
            qr_code.save()

            # Fetch the Ticket object and update status if conditions are met
            try:
                ticket = Ticket.objects.get(id=qr_code.ticket_id, status=2)
                ticket.status = 3
                ticket.save()

                # Prepare the success response with the QR code data
                response = {
                    'status': 'success',
                    'redirect_url': f'/scan-success/?ticket_id={ticket_id}&ticket_level={ticket_level}&event={event}&price={price}'
                }
                return JsonResponse(response)
            except Ticket.DoesNotExist:
                # If Ticket with specified ID and status=2 does not exist
                return redirect('scan-failed')
        
        except:
            # Handle various possible exceptions that could occur during data processing
            return redirect('scan-failed')

    # If request method is not POST
    return JsonResponse({'status': 'error'}, status=400)


def scan_success(request):
    ticket_id = request.GET.get('ticket_id')
    ticket_level = request.GET.get('ticket_level')
    event = request.GET.get('event')
    price = request.GET.get('price')
    
    qr_code = {
        'ticket_id': ticket_id,
        'ticket_level': ticket_level,
        'event': event,
        'price': price
    }
    
    return render(request, 'scan/success.html', {'qr_code': qr_code})
