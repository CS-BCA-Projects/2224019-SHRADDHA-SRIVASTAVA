from django import forms

class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    phone = forms.CharField(max_length=15, required=True)
    age = forms.IntegerField(required=True)
    menstruation_duration = forms.IntegerField(required=True)
    menstrual_flow = forms.ChoiceField(choices=[("Light", "Light"), ("Heavy", "Heavy"), ("Moderate", "Moderate")], required=True)
    skin_type = forms.ChoiceField(choices=[("Dry", "Dry"), ("Oily", "Oily"), ("Normal", "Normal")], required=True)
    itchiness = forms.ChoiceField(choices=[("Yes", "Yes"), ("No", "No")], required=True)
    password = forms.CharField(
        widget=forms.PasswordInput(),  # Masks the input
        required=True,
        min_length=8
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(),
        required=True,
        min_length=8
    )

    # ✅ Validate that passwords match
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")

        return cleaned_data

#created by me
class LoginForm(forms.Form):
    """User Login Form"""
    phone = forms.CharField(max_length=15, required=True)
    password = forms.CharField(widget=forms.PasswordInput)