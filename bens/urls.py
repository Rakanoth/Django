from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^$', views.bens_list),
    url(r'^(?P<bens_id>[0-9]+)/$', views.detail, name='detail'),
]