import ssl
import smtplib
from email.message import EmailMessage
from urllib import request

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order
from events.models import Ticket

@receiver(post_save, sender=Order)
def set_qr(sender, instance, created, **kwargs):
    if created:
        # Retrieve the first available ticket with status=1
        ticket = Ticket.objects.filter(status=1).first()

        if ticket:
            instance.qr_code = ticket
            ticket.status = 2
            ticket.save()
            instance.save()

@receiver(post_save, sender=Order)
def send_order_confirmation_email(sender, instance, created, **kwargs):
    if created:
        send_order_email(instance)

def send_order_email(order_instance):
    email_sender = "developer.udithsandaruwan@gmail.com"  # Replace with your email
    email_password = "fvcs gpoi vxwz roku"  # Replace with your email password or use environment variables
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
