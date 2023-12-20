# Generated by Django 4.2.7 on 2023-12-20 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0005_customuser_groups_customuser_user_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='TournamentImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.ImageField(upload_to='images/%Y/%m/%d')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.tournament', verbose_name='Турнир')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
                'db_table': 'images',
            },
        ),
    ]