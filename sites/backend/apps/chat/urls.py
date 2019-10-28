from django.urls import path

from apps.chat.views import ChatAppView, RoomView

urlpatterns = [
    path("", ChatAppView.as_view(), name="app"),
    path("<str:room_name>/", RoomView.as_view(), name="room"),
]
