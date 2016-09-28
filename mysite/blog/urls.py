from django.conf.urls import include, url

from . import views

app_name = "blog"
urlpatterns = [
# url(r'^$', views.hello, name='hello'),
url(r'^$', views.index, name='index'),
url(r'^(?P<post_id>[0-9]+)/$', views.detail, name='detail'),
url(r'^create/$', views.create, name='create'),


]
