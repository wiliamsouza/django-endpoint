from django.conf.urls import patterns, url


from .views import AuthorizationHomeList


urlpatterns = patterns(
    '',
    url(r'^$', AuthorizationHomeList.as_view(), name='authorization_home'),
)
