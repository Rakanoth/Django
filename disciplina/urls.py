from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^$', views.disciplinas_list),
    url(r'^(?P<disciplina_id>[0-9]+)/$', views.detail, name='detail'),
]