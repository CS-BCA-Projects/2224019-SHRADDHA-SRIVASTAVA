from django import forms

class ChatForm(forms.Form):
    message = forms.CharField(max_length=500, required=True)