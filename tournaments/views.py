from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views import View

from tournaments.forms import OrganizerRegistrationForm


def logout_view(request):
    logout(request)
    return redirect('')


def home_view(request):
    return render(request, 'home.html')


def organizer_registration_view(request):
    if request.method == 'GET':
        form = OrganizerRegistrationForm()
        return render(request, 'organizer_registration.html', {'form': form})

    if request.method == 'POST':
        form = OrganizerRegistrationForm(request.POST)
        if form.is_valid:
            user = form.save(commit=False)
            return render(request, 'home.html', {'form': form})

        return render(request, 'organizer_registration.html', {'form': form})
