from django.conf.urls import *
from main.views import *
from views import *

urlpatterns = patterns('',
                       url(r'^$', hello),
                       url(r'^send/', save),
                       )