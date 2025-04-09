# project_tracker/forms.py
from django import forms
import re


class PeriodTrackerForm(forms.Form):
    last_period_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        required=True
    )
    cycle_length = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'min': '21', 'max': '35'}),
        required=True,
        initial=28
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=15,
        required=False
    )
    sms_enabled = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        required=False
    )

    # ✅ Extra fields matching your HTML form
    mood = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False
    )
    water_intake = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        required=False
    )
    cravings = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Chocolate, ice cream, etc.'}),
        required=False
    )

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        sms_enabled = self.cleaned_data.get('sms_enabled')

        if sms_enabled and not phone_number:
            raise forms.ValidationError("Phone number is required if SMS is enabled.")
        
        if phone_number and not re.match(r'^\+?\d{10,15}$', phone_number):
            raise forms.ValidationError("Phone number must be in E.164 format (e.g., +919876543210)")
        
        return phone_number