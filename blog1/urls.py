from django.contrib import admin
from django.conf.urls import url

from . import views

urlpatterns = [
    # url('admin/', admin.site.urls),
    url('^$', views.index),
    url('register/', views.register),
    url('login/', views.login),
]
