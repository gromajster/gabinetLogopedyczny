import datetime

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    published_date = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    long_text = models.TextField(max_length=1000)
    published = models.BooleanField(default=False)
