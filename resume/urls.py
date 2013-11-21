from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/personal/', 'main.views.main'),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^', include('main.urls')),
)

urlpatterns += staticfiles_urlpatterns()
