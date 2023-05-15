# Generated by Django 4.0.5 on 2023-05-14 18:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_alter_player_end_time_alter_player_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 14, 18, 50, 19, 809239, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='player',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 14, 18, 50, 19, 809239, tzinfo=utc)),
        ),
    ]
