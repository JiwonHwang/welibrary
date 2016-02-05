from django.conf.urls import url, include
from . import views


urlpatterns = [
    # ex: /note/
    url(r'^$', views.index, name='index'),
    # ex: /note/about/
    url(r'^about/$', views.about, name='about'),
    # ex: /note/post/list/
    url(r'^post/list/$', views.post_list, name='post_list')
    # ex: /note/post/detail/
    url(r'^post/detail/$', views.post_detail, name="post_detail")
]



