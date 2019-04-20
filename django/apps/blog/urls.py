from django.conf.urls import url

from . import feeds, views


urlpatterns = [
    url(r'^$', views.listing, name='listing'),
    url(r'^(?P<pk>\d+)(?:/(?P<slug>[^/]+))?/$', views.detail, name='detail'),
    url(r'^feed/$', feeds.BlogFeed(), name='feed'),
]
