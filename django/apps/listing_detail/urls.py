from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.listing, name='listing'),
    url(r'^(?P<pk>\d+)(?:/(?P<slug>[^/]+))?/$', views.detail, name='detail'),
]
