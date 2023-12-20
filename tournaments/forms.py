from django import forms
from .models import Organizer


class OrganizerRegistrationForm(forms.ModelForm):
    title = forms.CharField(max_length=50, label='Наименование')
    email = forms.EmailField(max_length=256, label='Email')
    password = forms.CharField(widget=forms.PasswordInput(), label='Пароль')
    passwordConfirm = forms.CharField(widget=forms.PasswordInput(), label='Пароль повторно')

    class Meta:
        model = Organizer
        fields = ['title', 'email', 'password', 'passwordConfirm']
