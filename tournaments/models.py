from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User, AbstractUser, PermissionsMixin
from django.db import models

from tournaments.custom_user_manager import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email: str = models.EmailField(max_length=256, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Organizer(models.Model):
    title: str = models.CharField(
        max_length=50,
        verbose_name='Наименование')

    user: CustomUser = models.OneToOneField(
        to=CustomUser,
        related_name='organizer',
        on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'organizer'
        verbose_name = 'Организатор',
        verbose_name_plural = 'Организаторы'


class Tournament(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Наименование')
    description = models.CharField(
        max_length=400,
        verbose_name='Описание')
    organizer = models.ForeignKey(
        to=Organizer,
        on_delete=models.CASCADE,
        verbose_name='Организатор')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'tournament'
        verbose_name = 'Турнир',
        verbose_name_plural = 'Турниры'


class TournamentImage(models.Model):
    content = models.ImageField(upload_to='images/%Y/%m/%d')
    book: Tournament = models.ForeignKey(
        to=Tournament,
        verbose_name='Турнир',
        on_delete=models.CASCADE)

    def __str__(self):
        return str(self.content)

    class Meta:
        db_table = 'images'
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class Player(models.Model):
    user: CustomUser = models.OneToOneField(
        to=CustomUser,
        related_name='player',
        on_delete=models.CASCADE)

    name: str = models.CharField(
        max_length=50,
        verbose_name='Имя')
    surname: str = models.CharField(
        max_length=50,
        verbose_name='Фамилия')
    patronymic: str = models.CharField(
        max_length=50,
        verbose_name='Отчество')

    def __str__(self):
        return self.surname + ' ' + self.name + ' ' + self.patronymic

    class Meta:
        db_table = 'players'
        verbose_name = 'Игрок',
        verbose_name_plural = 'Игроки'


class TournamentPlayer(models.Model):
    tournament: Tournament = models.ForeignKey(
        to=Tournament,
        verbose_name='Турнир',
        on_delete=models.CASCADE)
    player: Player = models.ForeignKey(
        to=Player,
        verbose_name='Игрок',
        on_delete=models.CASCADE)

    def __str__(self):
        return 'Игрок ' + self.player + ' на турнире ' + self.tournament

    class Meta:
        db_table = 'tournament_players'
        verbose_name = 'Участник турнира',
        verbose_name_plural = 'Участники турнира'


class Referee(models.Model):
    user: CustomUser = models.OneToOneField(
        to=CustomUser,
        related_name='referee',
        on_delete=models.CASCADE)

    name: str = models.CharField(
        max_length=50,
        verbose_name='Имя')
    surname: str = models.CharField(
        max_length=50,
        verbose_name='Фамилия')
    patronymic: str = models.CharField(
        max_length=50,
        verbose_name='Отчество')

    def __str__(self):
        return self.surname + ' ' + self.name + ' ' + self.patronymic

    class Meta:
        db_table = 'referees'
        verbose_name = 'Судья',
        verbose_name_plural = 'Судьи'


class TournamentReferee(models.Model):
    referee: Referee = models.ForeignKey(
        to=Referee,
        verbose_name='Судья',
        on_delete=models.CASCADE)
    tournament: Tournament = models.ForeignKey(
        to=Tournament,
        verbose_name='Турнир',
        on_delete=models.CASCADE)

    def __str__(self):
        return self.referee

    class Meta:
        db_table = 'tournament_referees'
        verbose_name = 'Судья партии',
        verbose_name_plural = 'Судьи партий'


class Game(models.Model):
    tournament: Tournament = models.ForeignKey(
        to=Tournament,
        verbose_name='Турнир',
        on_delete=models.CASCADE)
    tournament_referee: TournamentReferee = models.ForeignKey(
        to=TournamentReferee,
        verbose_name="Судья партии",
        on_delete=models.CASCADE),
    first_player: Player = models.ForeignKey(
        to=Player,
        verbose_name='Первый игрок',
        related_name='first_player',
        on_delete=models.CASCADE)
    second_player: Player = models.ForeignKey(
        to=Player,
        verbose_name='Второй игрок',
        related_name='second_player',
        on_delete=models.CASCADE)

    def __str__(self):
        return 'Партия между ' + self.first_player + ' и ' + self.second_player

    class Meta:
        db_table = 'games'
        verbose_name = 'Партия',
        verbose_name_plural = 'Партии'
