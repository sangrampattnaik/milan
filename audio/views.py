from . import serializers, models
from rest_framework import viewsets, parsers


class SongViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SongSerializer
    queryset = models.Song.objects.all()
    parser_classes = [parsers.FormParser,parsers.MultiPartParser]

class AudiobookViewSet(viewsets.ModelViewSet):
    parser_classes = [parsers.FormParser,parsers.MultiPartParser]
    serializer_class = serializers.AudiobookSerializer
    queryset = models.Audiobook.objects.all()

class PodcastViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PodcastSerializer
    queryset = models.Podcast.objects.all()
    parser_classes = [parsers.FormParser,parsers.MultiPartParser]