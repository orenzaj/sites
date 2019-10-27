from django.views.generic import TemplateView
from rest_framework import viewsets

from sites.orenza import models, serializers


class Orenza(TemplateView):
    template_name = "sites/orenza/index.html"


class CheatSheetView(viewsets.ModelViewSet):
    queryset = models.CheatSheet.objects.all()
    serializer_class = serializers.CheatSheetSerializer


class CheatSheetListView(TemplateView):
    template_name = "sites/orenza/bulma.html"
