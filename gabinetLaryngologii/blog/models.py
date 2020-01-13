import datetime

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    published_date = models.DateField(auto_now=False)
    published_time = models.TimeField(auto_now=False)
    picture_url = models.FileField(upload_to='blog_pictures/', blank=True, null=True)
    long_text = models.TextField(max_length=1000)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
