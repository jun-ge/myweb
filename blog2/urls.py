from django.contrib import admin
from django.conf.urls import url

from . import views

urlpatterns = [
    # url('^admin/', admin.site.urls),
    url('^$', views.index),
    url('login/', views.login),
    url('register/', views.register),
]