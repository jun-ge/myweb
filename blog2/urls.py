from django.contrib import admin
from django.conf.urls import url

from blog1 import views

urlpatterns = [
    # url('^admin/', admin.site.urls),
    url('^$', views.index),
]