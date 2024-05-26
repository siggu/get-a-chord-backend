from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Chord


class ChordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chord
        fields = "__all__"
