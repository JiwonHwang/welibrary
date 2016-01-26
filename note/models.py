import datetime

from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=50)
    created_date = models.DateTimeField('created_date')
    published_date = models.DateTimeField('published_date')
    content = models.TextField()
    photo = models.ImageField(blank=True)
    link = models.URLField(blank=True)


    def __str__(self):
        return self.title

