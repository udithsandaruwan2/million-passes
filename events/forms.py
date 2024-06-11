from django.forms import ModelForm

from .models import Event, TicketPrices

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'featured_image', 'date_time', 'location']
        
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control'}
        )
        
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control'}
        )
        
        self.fields['featured_image'].widget.attrs.update(
            {'class': 'form-control'}
        )
        
        self.fields['date_time'].widget.attrs.update(
            {'class': 'form-control', 'id': 'datetime-picker'}
        )
        
        self.fields['location'].widget.attrs.update(
            {'class': 'form-control'}
        )
        
class TicketForm(ModelForm):
    class Meta:
        model = TicketPrices
        fields = ['name', 'event', 'price', 'amount']
        
        
    def __init__(self, *args, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)
        
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control'}
        )
        
        self.fields['event'].widget.attrs.update(
            {'class': 'form-control'}
        )
        
        self.fields['price'].widget.attrs.update(
            {'class': 'form-control'}
        )
        
        self.fields['amount'].widget.attrs.update(
            {'class': 'form-control'}
        )