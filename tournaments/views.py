import random

from django.contrib.auth import logout, login, authenticate
from django.db import transaction, connection
from django.shortcuts import render, redirect

from tournaments.forms import OrganizerRegistrationForm, LoginForm, PlayerRegistrationForm, RefereeRegistrationForm, \
    CreateTournamentForm
from tournaments.models import CustomUser, Organizer, Player, Referee, Tournament, TournamentPlayer, TournamentReferee, \
    Game


def logout_view(request):
    logout(request)
    return redirect(home_view)


def home_view(request):
    if request.user.is_anonymous or request.user.is_superuser:
        tournaments = Tournament.objects.all()

        context = {
            'tournaments': tournaments
        }

        return render(request, 'home.html', context)

    if request.user.player:
        tournaments_without_player = Tournament.objects.exclude(tournamentplayer__player_id=request.user.player_id)

        context = {
            'tournaments': tournaments_without_player
        }

        return render(request, 'home.html', context)

    if request.user.referee:
        tournaments_without_referee = Tournament.objects.exclude(tournamentreferee__referee_id=request.user.referee_id)

        context = {
            'tournaments': tournaments_without_referee
        }

        return render(request, 'home.html', context)

    if request.user.organizer:
        tournaments_without_organizer = Tournament.objects.exclude(
            organizer_id=request.user.organizer_id)

        context = {
            'tournaments': tournaments_without_organizer
        }

        return render(request, 'home.html', context)


def my_tournaments_view(request):
    if request.user.organizer:
        tournaments = Tournament.objects.filter(organizer_id=request.user.organizer_id).all()

        context = {
            'tournaments': tournaments
        }

        return render(request, 'my_tournaments.html', context)

    if request.user.player:
        tournaments = Tournament.objects.filter(tournamentplayer__player_id=request.user.player_id)

        context = {
            'tournaments': tournaments
        }

        return render(request, 'my_tournaments.html', context)

    if request.user.referee:
        tournaments = Tournament.objects.filter(tournamentreferee__referee_id=request.user.referee_id)

        context = {
            'tournaments': tournaments
        }

        return render(request, 'my_tournaments.html', context)


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
            return redirect(home_view)

    return render(request, 'login.html')


@transaction.atomic
def mark_winner_view(request, game_id: int):
    game = Game.objects.get(id=game_id)
    game.score = 1
    game.save()

    relation_game = Game.objects.get(first_player=game.second_player, second_player=game.first_player)
    relation_game.score = 0

    relation_game.save()

    return redirect('tournament-detail', tournament_id=game.tournament_id)


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

            organizer = Organizer.objects.create(title=title)

            user = CustomUser.objects.create_user(email=email, password=password, organizer=organizer)

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

            player = Player.objects.create(
                name=name,
                surname=surname,
                patronymic=patronymic)

            user = CustomUser.objects.create_user(email=email, password=password, player=player)

            player.save()

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

            referee = Referee.objects.create(
                name=name,
                surname=surname,
                patronymic=patronymic)

            user = CustomUser.objects.create_user(email=email, password=password, referee=referee)

            referee.save()

            login(request, user)
            return render(request, 'home.html')

        return render(request, 'login.html')


@transaction.atomic
def create_tournament_view(request, organizer_id: int):
    if request.method == 'POST':
        form = CreateTournamentForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            player_count = form.cleaned_data['player_count']
            referee_count = form.cleaned_data['referee_count']
            image = request.FILES.get('image')

            tournament = Tournament(
                title=title,
                description=description,
                player_count=player_count,
                referee_count=referee_count,
                organizer_id=organizer_id,
                image=image)

            tournament.save()

            return render(request, 'my_tournaments.html')

    return render(request, 'create_tournament.html')


@transaction.atomic
def join_tournament_view(request, tournament_id: int):
    if request.user.player is not None:
        current_player = request.user.player

        tournament = Tournament.objects.get(id=tournament_id)

        exists = TournamentPlayer.objects.filter(tournament=tournament, player=current_player).exists()
        if exists:
            return render(request, 'home.html')

        tournament_player = TournamentPlayer(tournament=tournament, player=current_player)
        tournament_player.save()

        return render(request, 'home.html')

    if request.user.referee is not None:
        tournament = Tournament.objects.get(id=tournament_id)
        current_referee = request.user.referee

        if TournamentReferee.objects.filter(tournament=tournament, referee=current_referee).exists():
            return render(request, 'home.html')

        tournament_referee = TournamentReferee(tournament=tournament, referee=current_referee)
        tournament_referee.save()

        return render(request, 'home.html')

    return render(request, 'home.html')


@transaction.atomic
def start_tournament_view(request, tournament_id: int):
    if request.user.organizer is None:
        return redirect(home_view)

    tournament = Tournament.objects.get(id=tournament_id)

    if tournament.status != Tournament.Status.NoStart:
        return redirect(home_view)

    games = []

    tournament_referees = TournamentReferee.objects.filter(tournament=tournament).all()
    tournament_players = TournamentPlayer.objects.filter(tournament=tournament)

    valid_players_count = tournament.player_count >= tournament_players.count() >= 2
    valid_referee_count = tournament.referee_count >= tournament_referees.count() >= 1

    if not valid_players_count or not valid_referee_count:
        return redirect(my_tournaments_view)

    for first_tournament_referee in tournament_players:
        first_player = first_tournament_referee.player
        for second_tournament_player in tournament_players:
            second_player = second_tournament_player.player

            random_tournament_referee = random.choice(tournament_referees)

            game = Game(
                tournament=tournament,
                tournament_referee=random_tournament_referee,
                first_player=first_player,
                second_player=second_player)

            games.append(game)

    Game.objects.bulk_create(games)
    tournament.status = Tournament.Status.Processing
    tournament.save()

    return redirect(my_tournaments_view)


@transaction.atomic
def leave_tournament_view(request, tournament_id: int):
    if request.user.player:
        player = request.user.player

        tournament_player = TournamentPlayer.objects.get(tournament_id=tournament_id, player=player)

        tournament_player.delete()
        return redirect(my_tournaments_view)

    if request.user.referee:
        referee = request.user.referee

        tournament_referee = TournamentReferee.objects.get(tournament_id=tournament_id, referee=referee)

        tournament_referee.delete()
        return redirect(my_tournaments_view)

    return redirect(my_tournaments_view)


def tournament_detail_view(request, tournament_id: int):
    tournament = Tournament.objects.get(id=tournament_id)

    players = Player.objects.filter(tournamentplayer__tournament_id=tournament_id).order_by('surname', 'name', 'patronymic')

    referee = Referee.objects.filter(tournamentreferee__tournament_id=tournament_id).order_by('surname', 'name', 'patronymic')

    games = Game.objects.filter(tournament=tournament).order_by('first_player__surname', 'first_player__name', 'first_player__patronymic', 'second_player__surname', 'second_player__name', 'second_player__patronymic')

    winners = Player.objects.raw(
        '''
select row_number() over(order by sum(g.score) desc) as id,
       p.surname,
       p.name,
       p.patronymic
from players p
         inner join tournament_players tp on p.id = tp.player_id
         inner join games g on p.id = g.first_player_id
group by p.surname,
         p.name,
         p.patronymic
order by sum(g.score) desc
limit 3
            '''
    )

    context = {
        'tournament': tournament,
        'players': players,
        'referees': referee,
        'games': games,
        'no_start': Tournament.Status.NoStart,
        'winners': winners
    }

    return render(request, 'tournament-detail.html', context)


@transaction.atomic
def completed_tournament_view(request, tournament_id: int):
    tournament = Tournament.objects.get(id=tournament_id)
    if tournament.status != Tournament.Status.Processing:
        return render(my_tournaments_view)

    tournament.status = Tournament.Status.Сompleted
    tournament.save()

    return redirect('tournament-detail', tournament_id=tournament_id)
