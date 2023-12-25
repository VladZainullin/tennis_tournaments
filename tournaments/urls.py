from django.urls import path

from tournaments.views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('logout/', logout_view, name='logout'),
    path('organizer-registration', organizer_registration_view, name='organizer-registration'),
    path('player-registration', player_registration_view, name='player-registration'),
    path('referee-registration', referee_registration_view, name='referee-registration'),
    path('my-tournaments', my_tournaments_view, name='my-tournaments'),
    path('login', login_view, name='login'),
    path('create-tournament/<int:organizer_id>', create_tournament_view, name='create-tournament'),
    path('join-tournament/<int:tournament_id>', join_tournament_view, name='join-tournament'),
    path('leave-tournament/<int:tournament_id>', leave_tournament_view, name='leave-tournament'),
    path('tournament-detail/<int:tournament_id>', tournament_detail_view, name='tournament-detail'),
    path('start-tournament/<int:tournament_id>', start_tournament_view, name='start-tournament'),
    path('mark-winner/<int:game_id>', mark_winner_view, name='mark-winner'),
    path('completed-tournament/<int:tournament_id>', completed_tournament_view, name='completed-tournament')
]
