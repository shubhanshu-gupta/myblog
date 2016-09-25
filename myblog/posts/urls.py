from django.conf.urls import include, url
from django.contrib import admin

from .views import (
	fetch_post,
	create_post,
	detail_post,
	update_post,
	delete_post,
	)

urlpatterns = [
    url(r'^$', fetch_post),
    url(r'^create/(?P<id>\d+)/$', create_post, name="show"),
    url(r'^detail/$', detail_post),
    url(r'^(?P<id>\d+)/edit/$', update_post, name='update'),
    url(r'^delete/$', delete_post),
]
