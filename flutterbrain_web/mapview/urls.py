# -*- encoding: utf-8 -*-

from django.conf.urls import include, url

from .views import index

urlpatterns = [
    url(r'^$', index, name="index"),
]

