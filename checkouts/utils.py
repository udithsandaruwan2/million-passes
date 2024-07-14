from email.message import EmailMessage
import smtplib
import ssl
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



def send_order_email(order_instance):
    email_sender = "quotexworkspace0@gmail.com"  # Replace with your email
    email_password = "mjlw vvsy mtpc bqfp"  # Replace with your email password or use environment variables
    email_receiver = order_instance.email
    email_subject = "Your Order Confirmation"
    email_body = f"Dear {order_instance.first_name},\n\nThank you for your order. Please find your ticket attached."

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = email_subject
    em.set_content(email_body)

    # Assuming qr_code is a field in Order pointing to a Ticket instance
    with open(order_instance.qr_code.qr_code.path, 'rb') as f:
        em.add_attachment(f.read(), maintype='image', subtype='png', filename=order_instance.qr_code.qr_code.name)

    # Establish SMTP connection using starttls() for Gmail
    try:
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls(context=ssl.create_default_context())
        smtp.login(email_sender, email_password)
        smtp.send_message(em)
    except Exception as e:
        print(f"Error sending email: {str(e)}")
    finally:
        smtp.quit()
