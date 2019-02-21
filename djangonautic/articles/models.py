# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    #add in thumbnail

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:500] + "..."



#python manage.py makemigration (For creating a new db eg, a new class)
#python manage.py migrate
