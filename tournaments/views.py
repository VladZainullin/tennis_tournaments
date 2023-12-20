from django.contrib.auth import logout, login, authenticate
from django.db import transaction
from django.shortcuts import render, redirect

from tournaments.forms import OrganizerRegistrationForm, LoginForm
from tournaments.models import CustomUser, Organizer


def logout_view(request):
    logout(request)
    return redirect(home_view)


def home_view(request):
    return render(request, 'home.html')


def login_view(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, email=email, password=password)
            if user is None:
                return render(request, 'login.html', {'form': form})

            login(request, user)
            return render(request, 'home.html')

    return render(request, 'login.html')


@transaction.atomic
def organizer_registration_view(request):
    if request.method == 'GET':
        form = OrganizerRegistrationForm()
        return render(request, 'organizer_registration.html', {'form': form})

    if request.method == 'POST':
        form = OrganizerRegistrationForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = CustomUser.objects.create_user(email=email, password=password)

            organizer = Organizer.objects.create(title=title, user=user)
            organizer.save()

            login(request, user)
            return render(request, 'home.html')

        return render(request, 'login.html', {'form': form})
