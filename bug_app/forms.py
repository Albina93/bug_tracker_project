from django import forms
from . import models

class AddTicketForm(forms.ModelForm):
    class Meta:
        model = models.TicketModel
        fields = ['title', 'description']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)