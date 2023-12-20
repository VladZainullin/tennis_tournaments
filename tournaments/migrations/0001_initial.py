# Generated by Django 4.2.7 on 2023-12-20 10:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=256, unique=True)),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Наименование')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='organizer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': ('Организатор',),
                'verbose_name_plural': 'Организаторы',
                'db_table': 'organizer',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=50, verbose_name='Отчество')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='player', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': ('Игрок',),
                'verbose_name_plural': 'Игроки',
                'db_table': 'players',
            },
        ),
        migrations.CreateModel(
            name='Referee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=50, verbose_name='Отчество')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='referee', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': ('Судья',),
                'verbose_name_plural': 'Судьи',
                'db_table': 'referees',
            },
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Наименование')),
                ('description', models.CharField(max_length=400, verbose_name='Описание')),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.organizer', verbose_name='Организатор')),
            ],
            options={
                'verbose_name': ('Турнир',),
                'verbose_name_plural': 'Турниры',
                'db_table': 'tournament',
            },
        ),
        migrations.CreateModel(
            name='TournamentReferee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.referee', verbose_name='Судья')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.tournament', verbose_name='Турнир')),
            ],
            options={
                'verbose_name': ('Судья партии',),
                'verbose_name_plural': 'Судьи партий',
                'db_table': 'tournament_referees',
            },
        ),
        migrations.CreateModel(
            name='TournamentPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.player', verbose_name='Игрок')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.tournament', verbose_name='Турнир')),
            ],
            options={
                'verbose_name': ('Участник турнира',),
                'verbose_name_plural': 'Участники турнира',
                'db_table': 'tournament_players',
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first_player', to='tournaments.player', verbose_name='Первый игрок')),
                ('second_player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second_player', to='tournaments.player', verbose_name='Второй игрок')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.tournament', verbose_name='Турнир')),
            ],
            options={
                'verbose_name': ('Партия',),
                'verbose_name_plural': 'Партии',
                'db_table': 'games',
            },
        ),
    ]
