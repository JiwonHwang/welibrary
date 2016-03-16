from django.conf.urls import  patterns, include, url
from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns( '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page':'/'}),
    url(r'', include('note.urls', namespace='note')), # namespace='note'
    # url('', include('social.apps.django_app.urls', namespace='social')),
    # social apps// why it doesn't start from r? check the error
    url(r'^accounts/', include('accounts.urls', namespace="accounts")),
)