from django.db import models


class Chord(models.Model):
    strings = models.CharField(max_length=15)
    fingering = models.CharField(max_length=15)
    chordName = models.CharField(max_length=15)
    enharmonicChordName = models.CharField(max_length=15)
    voicingID = models.CharField(max_length=30)
    tones = models.CharField(max_length=20)


# # Create your models here.
# class Strings(models.Model):
#     """Strings model definition"""

#     strings = models.CharField(max_length=15)


# class Fingerings(models.Model):
#     """Fingerings model definition"""

#     fingerings = models.CharField(max_length=15)


# class ChordName(models.Model):
#     """ChordName model definition"""

#     chordName = models.CharField(max_length=20)
