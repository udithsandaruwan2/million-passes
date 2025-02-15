from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name':'Name', 
        }   
        
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control form-control p-3', 'placeholder': 'eg : Udith Sandaruwan', 'type':'text'},
        )

        self.fields['email'].widget.attrs.update(
            {'class': 'form-control form-control p-3', 'placeholder':'eg : udith@eventarc.com', 'type':'text'}
        )

        self.fields['username'].widget.attrs.update(
            {'class': 'form-control form-control p-3', 'placeholder': 'eg : udith002', 'type':'text'}
        )

        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control form-control p-3', 'placeholder': '*************', 'type':'password'}
        )

        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control form-control p-3', 'placeholder': '*************', 'type':'password'}
        )


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'username', 'location', 'short_intro', 'bio',
                'profile_image', 'social_x', 'social_linkedin', 'social_youtube', 'social_portfolio']
        
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control'}
        )
        
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control'}
        )
        
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control'}
        )
        
        self.fields['location'].widget.attrs.update(
            {'class': 'form-control'}
        )
        
        self.fields['short_intro'].widget.attrs.update(
            {'class': 'form-control'}
        )
        
        self.fields['bio'].widget.attrs.update(
            {'class': 'form-control'}
        )

        self.fields['profile_image'].widget.attrs.update(
            {'class': 'form-control', 'id':'formFile'}
        )
        
        
        self.fields['social_x'].widget.attrs.update(
            {'class': 'form-control'}
        )
        
        self.fields['social_linkedin'].widget.attrs.update(
            {'class': 'form-control'}
        )
        
        self.fields['social_youtube'].widget.attrs.update(
            {'class': 'form-control'}
        )
        
        self.fields['social_portfolio'].widget.attrs.update(
            {'class': 'form-control'}
        )
