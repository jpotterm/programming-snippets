from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.view, name='view'),
    url(r'^list/$', views.view, name='view'),
    url(r'^soft-slug-detail/(?P<pk>\d+)(?:/(?P<slug>[^/]+))?/$', views.view, name='view'),
]
