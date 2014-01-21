from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from main.views import mediaserver
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/personal/$', 'main.views.main'),
    url(r'^edit/(?P<id>\d+)/', 'main.views.edit'),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^media/(?P<path>.*)$', mediaserver),
    url(r'^(?P<year>\d+)/', include('main.urls')),
    url(r'^user/ajax/$', 'main.views.user_ajax'),
    url(r'^$', 'main.views.year'),
)

urlpatterns += staticfiles_urlpatterns()
