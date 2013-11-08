from django.conf.urls import *
from main.views import hello

urlpatterns = patterns('',
                       url(r'^$', hello),
                       )
