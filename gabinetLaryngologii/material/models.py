import os

from django.db import models


class Media(models.Model):
    media_name = models.CharField(max_length=100)
    media_url = models.FileField(upload_to='media/')
    media_description = models.CharField(max_length=150, default="Napisz tu coś")

    def extension(self):
        name, extension = os.path.splitext(self.media_url.name)
        return extension

    def __str__(self):
        return self.media_name
