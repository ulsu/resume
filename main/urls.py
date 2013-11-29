from django.conf.urls import *
from main.views import *
from views import *

urlpatterns = patterns('',

                       url(r'^$', hello),
                       url(r'^send/', save),
                       url(r'^faculty/(?P<str>\d+)', specialty),
                       url(r'^(?P<str>\w+)/', pages),
                       )