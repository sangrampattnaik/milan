from django.db import models
from rest_framework import serializers

def validate_audiofile(value):
    try:
        ext = value.content_type.split("/")[1].lower()
        if ext not in ['mp3','mpeg','flac','wav']:
            raise serializers.ValidationError("invalid audio file format... Onlu mp3, wav, flac")
        return value
    except ValueError:
        raise serializers.ValidationError("invalid audio file format... Onlu mp3, wav, flac")





class TimeStampMixin(models.Model):
    id = models.AutoField(primary_key=True,editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    audio_file = models.FileField(upload_to="audio_files",validators=[validate_audiofile])
    
    class Meta:
        abstract = True


class Song(TimeStampMixin):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    duration = models.PositiveBigIntegerField()
    


class Podcast(TimeStampMixin):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    duration = models.PositiveBigIntegerField()
    host = models.CharField(max_length=99)


class Audiobook(TimeStampMixin):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    narrator = models.CharField(max_length=100)
    duration = models.PositiveBigIntegerField()
    
