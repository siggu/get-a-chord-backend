from django.db import models


class Chord(models.Model):
    id = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=30, default="")
    chord_type = models.CharField(max_length=5, default="c")
    imageUrl = models.ImageField(default="")