from django.conf.urls import url, include
from . import views


urlpatterns = [
    # ex :/note/index/
    url(r'^index/$', views.index, name='index'),
    # ex: /note/post_list/
    url(r'^post/list/$', views.post_list, name='post_list'),
    # ex: /note/post_detail/
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    # ex: /note/post/new/
    url(r'^post/new/$', views.post_new, name='post_new'),
    # ex: /note/post/5/edit/
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]

