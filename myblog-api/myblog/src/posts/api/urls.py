from django.conf.urls import url
from django.contrib import admin

from .views import (
	PostListAPIView,
	PostDetailAPIView,
	PostDeleteAPIView,
	PostUpdateAPIView,
	)

urlpatterns = [
	url(r'^$', PostListAPIView.as_view(), name='list'),
    # url(r'^create/$', post_create),
    url(r'^(?P<pk>\d+)/$', PostDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/edit/$', PostUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<pk>[\w-]+)/delete/$', PostDeleteAPIView.as_view(), name='delete'),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]
