from django.contrib import admin
from .models import Event, Ticket, TicketLevel, MemberPass, Pass

admin.site.register(Event)
admin.site.register(TicketLevel)
admin.site.register(Ticket)
admin.site.register(MemberPass)
admin.site.register(Pass)
