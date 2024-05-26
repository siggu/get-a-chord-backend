from django.contrib import admin
from .models import Chord


# Register your models here.
@admin.register(Chord)
class ChordAdmin(admin.ModelAdmin):
    list_display = (
        "strings",
        "fingering",
        "chordName",
        "enharmonicChordName",
        "voicingID",
        "tones",
    )
