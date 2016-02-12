import datetime

from django.db import models
from django import forms

from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)

    # post categories
    PYTHON = "python"
    DJANGO = "django"
    FRONTEND = "frontend"
    POSTCATEGORY = (
        (PYTHON, 'python'),
        (DJANGO, 'django'),
        (FRONTEND, 'frontend'),
        )
    postcategory = models.CharField(max_length=10, choices=POSTCATEGORY, default=PYTHON)

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    content = models.TextField()
    photo = models.ImageField(blank=True)
    link = models.URLField(blank=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=70)
    subject = models.CharField(max_length=100)
    message = models.TextField()