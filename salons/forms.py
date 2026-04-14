from django import forms
from .models import SalonRequest

class SalonRequestForm(forms.ModelForm):
    class Meta:
        model = SalonRequest
        fields = '__all__'