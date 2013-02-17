from django.conf.urls import patterns, url


from .views import ConsoleHomeList


urlpatterns = patterns(
    '',
    url(r'^$', ConsoleHomeList.as_view(), name='console_home'),
)
