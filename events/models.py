from django.db import models
import uuid
from users.models import Profile
from djmoney.models.fields import MoneyField

class Event(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default='events/default.JPG', upload_to='events/')
    date_time = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

class TicketPrices(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='ticket_prices')
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='LKR')
    amount = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return f"{self.name} - {self.price}"

# Accessing TicketPrices from Event
    # event = Event.objects.get(id=some_event_id)
    # ticket_prices = event.ticket_prices
