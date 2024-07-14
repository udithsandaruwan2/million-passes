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

