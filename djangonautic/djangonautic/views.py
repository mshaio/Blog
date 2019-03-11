from django.http import HttpResponse
from django.shortcuts import render

#from .models import Article
from articles.models import Article

def homepage(request):
    """Renders blog's homepage"""
    #return HttpResponse("Homepage")
    return render(request,'homepage.html')

def ML(request):
    """Retrieves blogs based on the web category (will need to change this to the ML categories)"""
    articles = filter("WebDev")
    return render(request,'ML.html',{'articles':articles})

def cyber_security(request):
    """Retrieves blogs based on the cyber security category"""
    articles = filter("Security")
    return render(request,'cybersecurity.html',{'articles':articles})

def robotics(request):
    """Retrieves blogs based on the robotics category"""
    articles = filter("Robotics")
    return render(request,'robotics.html',{'articles':articles})
    #return HttpResponse("ML")
    #return render(request,'ML.html')

def django_article(request):
    """Retrieves Django Blog
    also retrieving the most recent 3 articles in the database
    """
    articles = Article.objects.all()
    article = articles.get(title="Learning Django")
    recent_articles = Article.objects.all().order_by("date")[:3]
    return render(request,'DjangoArticle.html',{'article':article, 'recent_articles':recent_articles})

def filter(blog_category):
    """Filters the articles by date and by blog category"""
    articles = Article.objects.all().order_by("date") #retrieves article from db by date
    articles = articles.filter(category=blog_category) #Then filter it by Category
    return articles
