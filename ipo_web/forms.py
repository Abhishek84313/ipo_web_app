from django import forms
from .models import IPOInfo

class IPOInfoForm(forms.ModelForm):
    class Meta:
        model = IPOInfo
        fields = ['company_name', 'ipo_date', 'price']
        widgets = {
            'ipo_date': forms.DateInput(attrs={'type': 'date'}),
        }
