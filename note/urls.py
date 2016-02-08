from django.conf.urls import url, include
from . import views


urlpatterns = [
    # ex: /note/
    url(r'^$', views.index, name='index'),
    # ex: /note/about/
    url(r'^about/$', views.about, name='about'),


    # post list and details ex----------------------------
    # ex: /note/posts
    url(r'^posts/$', views.post_list, name='post_list'),
    # ex: /note/post/#
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name="post_detail"),


    # list of each category, need to ad detail.html of each-------------------------
    # ex: /note/python/
    url(r'^python/$', views.python_list, name='python_list'),
    # ex: /note/python/#
    url(r'^python/(?P<pk>[0-9]+)/$', views.python_detail, name="python_detail"),


    # ex: /note/django/
    url(r'^django/$', views.django_list, name='django_list'),
    # ex: /note/django/#
    url(r'^django/(?P<pk>[0-9]+)/$', views.django_detail, name='django_detail'),


    # ex: /note/frontend/
    url(r'^frontend/$', views.frontend_list, name='frontend_list'),
    # ex: /note/frontend/#
    url(r'^frontend/(?P<pk>[0-9]+)/$', views.frontend_detail, name='frontend_detail'),


    # ex: /note/contact/
    url(r'^contact/$', views.new_contact, name='new_contact'),
]



