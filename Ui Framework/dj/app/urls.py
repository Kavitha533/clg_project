from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from . import views

urlpatterns=[
    url(r'^admin/', admin.site.urls),
    path(r'', views.home),
    url(r'^page1/$', views.page1),
    url(r'^page2/$', views.page2),
    url(r'^page3/$', views.page3),
]