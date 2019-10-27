from django.views.generic import TemplateView
from rest_framework import viewsets

from apps.rhythm import models, serializers


class RhythmAppView(TemplateView):
    template_name = "apps/rhythm/index.html"


class SongView(viewsets.ModelViewSet):
    queryset = models.Song.objects.all()
    serializer_class = serializers.SongSerializer


class ArtistView(viewsets.ModelViewSet):
    queryset = models.Artist.objects.all()
    serializer_class = serializers.ArtistSerializer


class SoundView(viewsets.ModelViewSet):
    queryset = models.Sound.objects.all()
    serializer_class = serializers.SoundSerializer
