from django.db import models
import uuid
from users.models import Profile
from django.db import models
from django.conf import settings
from django.utils import timezone
import qrcode
import io
from django.core.files.base import ContentFile
import uuid
from io import BytesIO
from users.models import Profile

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


#we can get the this also as a member passes
class TicketLevel(models.Model):
    # STATUS_CHOICES = [
    #     (1, 'Default Pass'),
    #     (2, 'Member Pass'),

    # ]
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    created = models.DateTimeField(default=timezone.now)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    # status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    def __str__(self):
        return f"{self.name} for {self.event}"



def qr_code_upload_path(instance, filename):
    # Generates the upload path: qr_codes/ticket_level/<filename>
    return f'qr_codes/{instance.ticket_level}/{filename}'
class Ticket(models.Model): 
    STATUS_CHOICES = [
        (1, 'Available'),
        (2, 'Assigned'),
        (3, 'Used')
    ]

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    ticket_level = models.ForeignKey(TicketLevel, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    qr_code = models.ImageField(upload_to=qr_code_upload_path, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    
    def save(self, *args, **kwargs):
        if not self.qr_code:
            self.generate_qr_code()
        super().save(*args, **kwargs)

    def generate_qr_code(self):
        qr_data = f"Ticket ID: {self.id}, Ticket Level: {self.ticket_level}, Event: {self.ticket_level.event}, Price: {self.ticket_level.price}"
        qr = qrcode.make(qr_data)
        buffer = BytesIO()
        qr.save(buffer, format='PNG')
        file_name = f"qr_code_{self.id}.png"
        self.qr_code.save(file_name, ContentFile(buffer.getvalue()), save=False)

    def __str__(self):
        return str(self.id)
    
    
