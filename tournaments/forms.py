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


class PlayerRegistrationForm(forms.Form):
    name = forms.CharField(max_length=50, label='Имя')
    surname = forms.CharField(max_length=50, label='Фамилия')
    patronymic = forms.CharField(max_length=50, label='Отчество')
    email = forms.EmailField(max_length=256, label='Email')
    password = forms.CharField(widget=forms.PasswordInput(), label='Пароль')
    passwordConfirm = forms.CharField(widget=forms.PasswordInput(), label='Пароль повторно')

    class Meta:
        fields = ['name', 'surname', 'patronymic', 'email', 'password', 'passwordConfirm']


class RefereeRegistrationForm(forms.Form):
    name = forms.CharField(max_length=50, label='Имя')
    surname = forms.CharField(max_length=50, label='Фамилия')
    patronymic = forms.CharField(max_length=50, label='Отчество')
    email = forms.EmailField(max_length=256, label='Email')
    password = forms.CharField(widget=forms.PasswordInput(), label='Пароль')
    passwordConfirm = forms.CharField(widget=forms.PasswordInput(), label='Пароль повторно')

    class Meta:
        fields = ['name', 'surname', 'patronymic', 'email', 'password', 'passwordConfirm']


class LoginForm(forms.Form):
    email = forms.CharField(max_length=50, label='Наименование')
    password = forms.CharField(widget=forms.PasswordInput(), label='Пароль')

    class Meta:
        fields = ['email', 'password']


class CreateTournamentForm(forms.Form):
    title = forms.CharField(
        max_length=50,
        label='Наименование турнира')
    description = forms.CharField(
        max_length=1000,
        label='Наименование турнира')
    player_count = forms.IntegerField(
        min_value=1,
        label='Кол-во участников')
    referee_count = forms.IntegerField(
        min_value=1,
        label='Кол-во судей')
