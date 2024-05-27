from django.db import models


# Create your models here.
class Song(models.Model):

    name = models.CharField(max_length=50)
    desc = models.TextField()
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name='songs',
    )
