from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import *
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^login/', login),
    url(r'^logout/', logout),
    url(r'^register/', register),
)
