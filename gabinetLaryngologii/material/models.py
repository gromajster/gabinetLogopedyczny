from django.db import models


# Create your models here.

class Media(models.Model):
    media_name = models.CharField(max_length=100)
    media_url = models.FileField(upload_to='media/')
