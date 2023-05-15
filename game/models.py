from django.db import models
from django.contrib import admin
from django.utils import timezone

# Create your models here.
class Player(models.Model):
    def __str__(self):
        return self.username
    email=models.CharField(max_length=50)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    start_time=models.DateTimeField(default=timezone.now())
    end_time=models.DateTimeField(default=timezone.now())
    best_time=models.IntegerField(default=(10000000))
    curr_level=models.IntegerField(default=1)


