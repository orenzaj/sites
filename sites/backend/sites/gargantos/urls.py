from django.urls import path

from sites.gargantos.views import Gargantos

urlpatterns = [
    path("", Gargantos.as_view(), name="gargantos")
]
