from django.shortcuts import get_object_or_404
from django.shortcuts import render
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
    if request.method == 'POST':
        form = QRCodeForm(request.POST, request.FILES)
        if form.is_valid():
            qr_code_image = request.FILES['qr_code_image']
            qr_data = scan_qr_code(qr_code_image)

            if qr_data:
                # Attempt to parse QR code data
                try:
                    data_parts = qr_data.split(',')
                    qr_code = QRCode(
                        ticket_id=data_parts[0].split(':')[1].strip(),
                        ticket_level=data_parts[1].split(':')[1].strip(),
                        event=data_parts[2].split(':')[1].strip(),
                        price=int(data_parts[3].split(':')[1].strip())
                    )
                    qr_code.save()

                    # Check if the ticket with qr_code.ticket_id exists and its status is 2
                    ticket = Ticket.objects.get(id=qr_code.ticket_id,  status=2)

                    # If ticket exists and status is 2, update status to 3
                    ticket.status = 3
                    ticket.save()

                    return render(request, 'scan/success.html', {'qr_code': qr_code})

                except (IndexError, ValueError, Ticket.DoesNotExist):
                    # Handle the case where QR code data does not match expected format
                    # or ticket with qr_code.ticket_id does not exist or status is not 2
                    return render(request, 'scan/failure.html', {'error': 'Invalid QR code format or Already used.'})
            else:
                # Handle the case where QR code couldn't be scanned or is empty
                return render(request, 'scan/failure.html', {'error': 'Invalid QR code or could not be scanned.'})
        else:
            # Handle form validation errors
            return render(request, 'scan/failure.html', {'error': 'Form data is not valid.'})
    else:
        form = QRCodeForm()
    return render(request, 'scan/scan.html', {'form': form})

