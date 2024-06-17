from urllib import request
from django.forms import ModelForm
from django import forms

from .models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'mobile_number', 'verify_id']
        
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        
        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'type': 'text', 'id': 'first-name', 'placeholder': 'First Name'}
        )
        self.fields['first_name'].required = True

        self.fields['last_name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'type': 'text', 'id': 'last-name', 'placeholder': 'Last Name'}
        )
        self.fields['last_name'].required = True

        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'type': 'email', 'id': 'email', 'placeholder': 'Email Address'}
        )
        self.fields['email'].required = True

        self.fields['mobile_number'].widget.attrs.update(
            {'class': 'form-control mb-3', 'type': 'tel', 'id': 'phone', 'placeholder': 'Phone No'}
        )
        self.fields['mobile_number'].required = True

        self.fields['verify_id'].widget.attrs.update(
            {'class': 'form-control mb-3', 'type': 'text', 'id': 'id', 'placeholder': 'NIC / Passport / Driving License'}
        )
        self.fields['verify_id'].required = True
