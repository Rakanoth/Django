from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^$', views.candidatos_list),
    url(r'^(?P<candidato_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^candidato/new/$', views.candidato_new, name='candidato_new'),
    url(r'^candidato/(?P<pk>[0-9]+)/edit/$', views.candidato_edit, name='candidato_edit'),
]