from django.urls import path, include
from rest_framework import routers

from rhythm.views import SongView, ArtistView, RhythmAppView

router = routers.DefaultRouter()
router.register(r'songs', SongView, 'song')
router.register(r'artists', ArtistView, 'artist')

urlpatterns = [
    path("", RhythmAppView.as_view(), name="app"),
    path("api/", include(router.urls)),
]
