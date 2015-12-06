# -*- encoding: utf-8 -*-

from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^show_user/(?P<screen_name>[A-Za-z0-9_\-+=]+)/$', views.map, name="map"),
    url(r'^$', views.index, name="index"),
]

