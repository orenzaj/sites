from django.urls import path

from gargantos.views import Gargantos

urlpatterns = [
    path("", Gargantos.as_view())
]
