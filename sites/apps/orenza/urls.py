from django.urls import path

from orenza.views import Orenza

urlpatterns = [
    path("", Orenza.as_view())
]
