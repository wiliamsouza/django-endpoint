from __future__ import absolute_import, unicode_literals

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^api/console/', include('console.urls')),
    ##url(r'^api/authorization/', include('authorization.urls')),
)
