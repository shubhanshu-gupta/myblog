from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', "posts.views.fetch_post"),
    url(r'^create/$', "posts.views.create_post"),
    url(r'^detail/$', "posts.views.detail_post"),
    url(r'^update/$', "posts.views.update_post"),
    url(r'^delete/$', "posts.views.delete_post"),
]
