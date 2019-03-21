# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField
from tinymce.models import HTMLField
#from inline_media.fields import TextFieldWithInlines

# Create your models here.
class Article(models.Model):
    """Creates an article model"""
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    #body = HTMLField()
    #body = RichTextField()
    #body = models.TextFieldWithInlines() Does not work
    date = models.DateTimeField(auto_now_add=True)
    #add in thumbnail

    def __str__(self):
        """Retrieves blog title"""
        return self.title

    def snippet(self):
        """Retrieves first 500 characters of the blog content"""
        return self.body[:500] + "..."

    def content(self):
        """Retrieves blog content"""
        return self.body

    def slugs(self):
        return self.slug

    def retrieve_category(self):
        """Retrieves blog category"""
        return self.category

#python manage.py makemigrations (For creating a new db eg, a new class)
#python manage.py migrate
