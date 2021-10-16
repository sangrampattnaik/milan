from django.db import models


class TimeStampMixin(models.Model):
    id = models.AutoField(primary_key=True,editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
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
    
