# Generated by Django 4.0.5 on 2023-05-13 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_player_best_time_player_end_time_player_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='end_time',
            field=models.TimeField(default='00:00:00'),
        ),
        migrations.AlterField(
            model_name='player',
            name='start_time',
            field=models.TimeField(default='00:00:00'),
        ),
    ]