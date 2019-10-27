from rest_framework import serializers

from apps.rhythm import models


class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Song
        exclude = ["url"]



class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Artist
        exclude = ["url"]


class SoundSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Sound
        exclude = ["url"]
