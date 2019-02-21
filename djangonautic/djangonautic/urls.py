from django.conf.urls import url, include
from django.contrib import admin
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^articles/',include('articles.urls')),
    url(r'^ML/$',views.ML),
    url(r'^$',views.homepage),
]

urlpatterns += staticfiles_urlpatterns()