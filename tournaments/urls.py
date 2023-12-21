from django.urls import path

from tournaments.views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('logout/', logout_view, name='logout'),
    path('organizer-registration', organizer_registration_view, name='organizer-registration'),
    path('player-registration', player_registration_view, name='player-registration'),
    path('referee-registration', referee_registration_view, name='referee-registration'),
    path('organizer-tournaments/<int:organizer_id>', organizer_tournaments_view, name='organizer-tournaments'),
    path('login', login_view, name='login'),
    path('create-tournament/<int:organizer_id>', create_tournament_view, name='create-tournament'),
]
