from django.urls import path
from . import views

urlpatterns = [
    path("", views.Chords.as_view()),
    path("<str:chordName>", views.ChordDetail.as_view()),
]
