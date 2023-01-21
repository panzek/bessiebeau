from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'phone_number', 
            'street_address1', 
            'street_address2', 
            'town_or_city', 
            'county', 
            'postcode', 
            'country',
            'profile_image',
        ] 