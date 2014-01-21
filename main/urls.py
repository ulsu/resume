from django.conf.urls import *
from main.views import *
from views import *

urlpatterns = patterns('',
                       url(r'^$', hello),
                       url(r'^search', search),
                       url(r'^faculty/(?P<id>\d+)/', specialty),
                       url(r'^(?P<slug>\w+)/$', pages),
                       )