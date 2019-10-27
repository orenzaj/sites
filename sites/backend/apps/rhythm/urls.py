from django.urls import path

from apps.rhythm.views import RhythmAppView

urlpatterns = [
    path("", RhythmAppView.as_view(), name="app"),
]
