from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from . import serializers
from .serializers import ChordSerializer
from .models import Chord


class Chords(APIView):
    def get(self, request):
        chords = Chord.objects.all()
        serializer = ChordSerializer(
            chords,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.ChordSerializer(data=request.data)
        if serializer.is_valid():
            chord = serializer.save()
            return Response(serializers.ChordSerializer(chord).data)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )


class ChordDetail(APIView):
    def get_object(self, chordName):
        try:
            return Chord.objects.filter(chordName=chordName)
        except Chord.DoesNotExist:
            raise NotFound

    def get(self, request, chordName):
        chord = self.get_object(chordName)
        serializer = serializers.ChordSerializer(
            chord,
            many=True,
        )
        return Response(serializer.data)
