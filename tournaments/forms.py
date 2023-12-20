from django import forms
from .models import Organizer, CustomUser


class OrganizerRegistrationForm(forms.ModelForm):
    title = forms.CharField(max_length=50, label='Наименование')
    email = forms.EmailField(max_length=256, label='Email')
    password = forms.CharField(widget=forms.PasswordInput(), label='Пароль')
    passwordConfirm = forms.CharField(widget=forms.PasswordInput(), label='Пароль повторно')

    class Meta:
        model = Organizer
        fields = ['title', 'email', 'password', 'passwordConfirm']


class LoginForm(forms.Form):
    email = forms.CharField(max_length=50, label='Наименование')
    password = forms.CharField(widget=forms.PasswordInput(), label='Пароль')

    class Meta:
        fields = ['email', 'password']
