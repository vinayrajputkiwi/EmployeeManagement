from django import forms
from .models import checkin,checkout,registeremp

class checkinform(forms.ModelForm):
    class Meta:
        model= checkin
        fields=['first_name','last_name','email']

class checkoutform(forms.ModelForm):
    class Meta:
        model= checkout
        fields=['first_name','last_name','email']

class registerform(forms.ModelForm):
    class Meta:
        model= registeremp
        fields='__all__'