from rest_framework import viewsets
from django.views.generic import TemplateView

from rhythm.models import Artist, Song
from rhythm.serializers import ArtistSerializer, SongSerializer


class RhythmAppView(TemplateView):
    template_name = "rhythm/index.html"


class SongView(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class ArtistView(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
