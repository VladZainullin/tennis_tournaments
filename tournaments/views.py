from django.contrib.auth import logout, login, authenticate
from django.db import transaction
from django.shortcuts import render, redirect

from tournaments.forms import OrganizerRegistrationForm, LoginForm, PlayerRegistrationForm, RefereeRegistrationForm
from tournaments.models import CustomUser, Organizer, Player, Referee, Tournament


def logout_view(request):
    logout(request)
    return redirect(home_view)


def home_view(request):
    tournaments = Tournament.objects.all()

    context = {
        'tournaments': tournaments
    }

    return render(request, 'home.html', context)


@transaction.atomic
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


@transaction.atomic
def player_registration_view(request):
    if request.method == 'GET':
        return render(request, 'player_registration.html')

    if request.method == 'POST':
        form = PlayerRegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            patronymic = form.cleaned_data['patronymic']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = CustomUser.objects.create_user(email=email, password=password)

            organizer = Player.objects.create(
                name=name,
                surname=surname,
                patronymic=patronymic,
                user=user)

            organizer.save()

            login(request, user)
            return render(request, 'home.html')

        return render(request, 'login.html')


@transaction.atomic
def referee_registration_view(request):
    if request.method == 'GET':
        return render(request, 'referee_registration.html')

    if request.method == 'POST':
        form = RefereeRegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            patronymic = form.cleaned_data['patronymic']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = CustomUser.objects.create_user(email=email, password=password)

            organizer = Referee.objects.create(
                name=name,
                surname=surname,
                patronymic=patronymic,
                user=user)

            organizer.save()

            login(request, user)
            return render(request, 'home.html')

        return render(request, 'login.html')
