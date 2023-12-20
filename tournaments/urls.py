from django.urls import path

from tournaments.views import home_view, organizer_registration_view, logout_view

urlpatterns = [
    path('', home_view, name='home'),
    path('logout/', logout_view, name='logout'),
    path('organizer-registration', organizer_registration_view, name='organizer-registration')
]
