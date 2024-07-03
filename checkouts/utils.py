from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
import zipfile
from io import BytesIO
from django.http import HttpResponse
from events.models import Ticket

def filter_and_update_tickets(amount, level):
    tickets = Ticket.objects.filter(status=1, ticket_level=str(level))[:amount]
    if not tickets:
        return None

    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
        for ticket in tickets:
            if ticket.qr_code:
                # Update status
                ticket.status = 2
                ticket.save()

                # Add QR code to zip file
                qr_code_file = default_storage.open(ticket.qr_code.name)
                zip_file.writestr(ticket.qr_code.name, qr_code_file.read())

    zip_buffer.seek(0)
    return zip_buffer
