from django.contrib import admin
from tournaments.models import *


class TournamentAdmin(admin.ModelAdmin):
    readonly_fields = [f.name for f in TournamentPlayer._meta.get_fields()]
    list_filter = [f.name for f in Tournament._meta.get_fields() if f.name != 'id']
    search_fields = [f.name for f in Tournament._meta.get_fields() if f.name != 'id']


class TournamentRefereeAdmin(admin.ModelAdmin):
    list_filter = [f.name for f in TournamentReferee._meta.get_fields() if f.name != 'id']
    search_fields = [f.name for f in TournamentReferee._meta.get_fields() if f.name != 'id']


class TournamentPlayerAdmin(admin.ModelAdmin):
    list_filter = [f.name for f in TournamentPlayer._meta.get_fields() if f.name != 'id']
    search_fields = [f.name for f in TournamentPlayer._meta.get_fields() if f.name != 'id']


class GameAdmin(admin.ModelAdmin):
    list_filter = [f.name for f in Game._meta.get_fields() if f.name != 'id']
    search_fields = [f.name for f in Game._meta.get_fields() if f.name != 'id']


admin.site.register(Tournament)
admin.site.register(TournamentReferee)
admin.site.register(TournamentPlayer)
admin.site.register(Game)
