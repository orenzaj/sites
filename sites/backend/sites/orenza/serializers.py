from rest_framework import serializers

from sites.orenza import models


class CheatSheetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.CheatSheet
        exclude = ["url"]
