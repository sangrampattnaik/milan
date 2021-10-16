from . import serializers, models
from rest_framework import viewsets


class SongViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SongSerializer
    queryset = models.Song.objects.all()

class AudiobookViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AudiobookSerializer
    queryset = models.Audiobook.objects.all()

class PodcastViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PodcastSerializer
    queryset = models.Podcast.objects.all()