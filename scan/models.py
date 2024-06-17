from django.db import models

# Create your models here.
from django.db import models

class QRCode(models.Model):
    ticket_id = models.CharField(max_length=255)
    ticket_level = models.CharField(max_length=255)
    event = models.CharField(max_length=255)
    price = models.IntegerField()
    scanned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ticket_id
