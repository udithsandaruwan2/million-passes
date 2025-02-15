from urllib import request
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TicketLevel, Ticket, MemberPass, Pass


@receiver(post_save, sender=TicketLevel)
def create_tickets(sender, instance, created, **kwargs):
    if created:
        for _ in range(instance.quantity):
            Ticket.objects.create(ticket_level=instance)
            
        # profile = request.user.profile
        # TicketLevel.owner = profile
        # TicketLevel.save()
            


# @receiver(post_save, sender=Ticket)
# def update_ticket_level_quantity(sender, instance, **kwargs):
#     if instance.owner:
#         ticket_level = instance.ticket_level
#         ticket_level.quantity -= 1
#         ticket_level.save()


@receiver(post_save, sender=MemberPass)
def create_tickets(sender, instance, created, **kwargs):
    if created:
        for _ in range(instance.quantity):
            Pass.objects.create(_pass=instance)