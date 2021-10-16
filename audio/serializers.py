from rest_framework import serializers
from . import models


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Song
        fields = "__all__"

class AudiobookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Audiobook
        fields = "__all__"

class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Podcast
        fields = "__all__"

