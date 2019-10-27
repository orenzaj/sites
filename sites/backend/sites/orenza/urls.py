from django.urls import path

from sites.orenza.views import Orenza, CheatSheetListView

urlpatterns = [
    path("", Orenza.as_view()),
    path("cheatsheets/", CheatSheetListView.as_view())
]
