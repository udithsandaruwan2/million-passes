from django.contrib import admin
from .models import Event, Ticket, TicketLevel

admin.site.register(Event)
admin.site.register(TicketLevel)
admin.site.register(Ticket)
