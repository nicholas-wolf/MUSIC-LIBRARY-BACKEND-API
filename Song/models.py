from django.db import models
from datetime import date

# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    release_date = models.DateField(default=date.today)
    genre = models.CharField(max_length=255)