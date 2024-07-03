from urllib import request
from django.forms import ModelForm
from django import forms

from .models import Event, TicketLevel
from users.models import TeamMember

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
        
class TicketLevelForm(ModelForm):
    class Meta:
        model = TicketLevel
        fields = ['name', 'price', 'quantity']
        
    def __init__(self, *args, **kwargs):
        super(TicketLevelForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update(
            {'class': 'form-control'}
        )
        
        self.fields['price'].widget.attrs.update(
            {'class': 'form-control'}
        )
        
        self.fields['quantity'].widget.attrs.update(
            {'class': 'form-control'}
        )

class TeamMemberForm(ModelForm):
    class Meta:
        model = TeamMember
        fields = ['name', 'email', 'idn']
        
    def __init__(self, *args, **kwargs):
        super(TeamMemberForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update(
            {'class': 'form-control'}
        )
        
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control'}
        )
        
        self.fields['idn'].widget.attrs.update(
            {'class': 'form-control'}
        )