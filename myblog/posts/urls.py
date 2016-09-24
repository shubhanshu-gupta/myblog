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
    url(r'^create/$', create_post),
    url(r'^detail/$', detail_post),
    url(r'^update/$', update_post),
    url(r'^delete/$', delete_post),
]
