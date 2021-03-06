from django.conf.urls import url, include
from . import views


urlpatterns = [
    # ex: /
    url(r'^$', views.index, name='index'),
    # ex: /about/
    url(r'^about/$', views.about, name='about'),
    # ex: /drafts/
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),


    # post list and details ex----------------------------
    # ex: /posts/
    url(r'^posts/$', views.post_list, name='post_list'),
    # ex: /post/#
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name="post_detail"),
    # ex: /post/new/
    url(r'^post/new/$', views.post_new, name='post_new'),
    # ex: /post/#/edit/
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    # ex: /post/#/publish/
    url(r'^post/(?P<pk>[0-9]+)/publish/$', views.post_publish, name='post_publish'),
    # ex: /post/#/remove/
    url(r'^post/(?P<pk>[0-9]+)/remove/$', views.post_remove, name='post_remove'),
    # ex: /post/#/comment/
    url(r'^post/(?P<pk>[0-9]+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),

    # categories-------------------------
    # ex: /python/
    url(r'^python/$', views.python_list, name='python_list'),
    # ex: /python/#
    url(r'^python/(?P<pk>[0-9]+)/$', views.python_detail, name="python_detail"),
    # ex: /python/#/comment/
    url(r'^python/(?P<pk>[0-9]+)/comment/$', views.python_add_comment_to_post, name='python_add_comment_to_post'),

    # ex: /django/
    url(r'^django/$', views.django_list, name='django_list'),
    # ex: /django/#
    url(r'^django/(?P<pk>[0-9]+)/$', views.django_detail, name='django_detail'),
    # ex: /django/#/comment/
    url(r'^django/(?P<pk>[0-9]+)/comment/$', views.django_add_comment_to_post, name='django_add_comment_to_post'),


    # ex: /frontend/
    url(r'^frontend/$', views.frontend_list, name='frontend_list'),
    # ex: /frontend/#
    url(r'^frontend/(?P<pk>[0-9]+)/$', views.frontend_detail, name='frontend_detail'),
    # ex: /frontend/#/comment/
    url(r'^frontend/(?P<pk>[0-9]+)/comment/$', views.frontend_add_comment_to_post, name='frontend_add_comment_to_post'),


    # ex: /more/
    url(r'^more/$', views.more_list, name='more_list'),
    # ex: /more/#
    url(r'^more/(?P<pk>[0-9]+)/$', views.more_detail, name='more_detail'),
    # ex: /more/#/comment/
    url(r'more/(?P<pk>[0-9]+)/$', views.more_add_comment_to_post, name='more_add_comment_to_post'),


    #---------------------------------------
    # ex: /contact/contact/new/
    url(r'^contact/$', views.contact_new, name='contact_new'),

    #---------------------------------------
    # ex: /comment/#/approve/
    url(r'^comment/(?P<pk>[0-9]+)/approve/$', views.comment_approve, name='comment_approve'),
    # ex: /comment/#/remove/
    url(r'^comment/(?P<pk>[0-9]+)/remove/$', views.comment_remove, name='comment_remove'),
]



