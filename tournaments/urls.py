from django.urls import path

from tournaments.views import home_view

urlpatterns = [
    path('', home_view, name='home'),
]
