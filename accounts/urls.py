from django.conf.urls import include, urls

from . import views

urlpatterns = [
    url('^register/', views.register, name="register",),
    url('^logout/', vies.logout, name="logout",),
    url('^', include('django.contrib.auth.urls')),
]