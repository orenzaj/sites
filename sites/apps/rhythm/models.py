from django.db import models


class Song(models.Model):
    title = models.CharField(
        max_length=100,
        null=True
    )


class Artist(models.Model):
    name = models.CharField(
        max_length=100,
        default=''
    )
