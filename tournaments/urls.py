from django.urls import path

from tournaments.views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('logout/', logout_view, name='logout'),
    path('organizer-registration', organizer_registration_view, name='organizer-registration'),
    path('player-registration', player_registration_view, name='player-registration'),
    path('referee-registration', referee_registration_view, name='referee-registration'),
    path('login', login_view, name='login')
]
