from django.db import models

class CheatSheet(models.Model):
    topic = models.CharField(
        max_length=100,
        null=True
    )
