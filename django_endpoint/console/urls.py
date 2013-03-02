from __future__ import absolute_import, unicode_literals

from django.conf.urls import patterns, url


from .views import (ConsoleHomeList, BrandingInformationUpdate,
                    ClientIdentifierCreate, ClientIdentifierUpdate)


urlpatterns = patterns(
    '',
    url(r'^$', ConsoleHomeList.as_view(), name='console_home'),
    url(r'branding/information/(?P<pk>\d+)/$',
        BrandingInformationUpdate.as_view(),
        name='branding_information_update'),
    url(r'client/identifier/add/$',
        ClientIdentifierCreate.as_view(),
        name='client_identifier_add'),
    url(r'client/identifier/(?P<pk>\d+)/$',
        ClientIdentifierUpdate.as_view(),
        name='client_identifier_update'),
)
