import uuid
import random
from django.db import models


from events.models import Ticket, TicketLevel
from users.models import Profile

def generate_order_id():
    return ''.join(random.choices('0123456789', k=8))

class Order(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    ticket_level = models.ForeignKey(TicketLevel, on_delete=models.CASCADE, null=True, blank=True)
    ticket_levels = models.JSONField(null=True, blank=True)
    ticket_quantity = models.PositiveIntegerField(default=1)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    mobile_number = models.CharField(max_length=15, null=True, blank=True)
    verify_id = models.CharField(max_length=50, null=True, blank=True)
    order_id = models.CharField(max_length=8, default=generate_order_id, unique=True)
    stripe_payment_token = models.CharField(max_length=255, null=True, blank=True)
    qr_code = models.OneToOneField(Ticket, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return str(self.id)
