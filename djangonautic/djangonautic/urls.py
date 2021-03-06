from django.conf.urls import url, include
from django.contrib import admin
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^articles/',include('articles.urls')),
    url(r'^ML/$',views.ML),
    url(r'^ML/learning-django/$',views.django_article),
    url(r'^cybersecurity/$',views.cyber_security),
    url(r'^robotics/$',views.robotics),
    url(r'^$',views.homepage),
]

urlpatterns += staticfiles_urlpatterns()
