from django.contrib.auth.forms import UserCreationForm

from tournaments.models import Organizer


class OrganizerRegistrationForm(UserCreationForm):
    class Meta:
        model = Organizer
        fields = ['title', 'password1', 'password2']
