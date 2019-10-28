from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from django.urls import include, path
from rest_framework import routers

from apps.chat import routing
from apps.rhythm.views import (ArtistView, SongView, SoundView)
from sites.orenza.views import CheatSheetView

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
})

router = routers.DefaultRouter()
router.register(r'songs', SongView, 'song')
router.register(r'artists', ArtistView, 'artist')
router.register(r'sounds', SoundView, 'sound')
router.register(r'cheatsheets', CheatSheetView, 'cheatsheet')

urlpatterns = [
    # Sites
    path('sites/', include('sites.urls'), name="sites"),

    # Apps
    path('apps/', include('apps.urls'), name="apps"),

    # API
    path("api/", include(router.urls)),
]
