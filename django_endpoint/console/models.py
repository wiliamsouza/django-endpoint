from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class BrandingInformation(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=255)
    logo = models.CharField(max_length=255)  # Max size 120x60 pixels
    home_page_url = models.CharField(max_length=255)


class ClientID(models.Model):

    SERVICE_ACCOUNT = 'S'
    WEB_APP = 'W'
    INSTALLED_APP = 'I'
    APP_TYPE_CHOICES = (
        (SERVICE_ACCOUNT, _('Service account')),
        (WEB_APP, _('Web application')),
        (INSTALLED_APP, _('Installed application')),
    )

    ANDROID = 'A'
    CHROME_APP = 'C'
    IOS = 'I'
    OTHER = 'O'
    INSTALLED_APP_TYPE_CHOICES = (
        (ANDROID,  _('Android')),
        (CHROME_APP, _('Chrome application')),
        (IOS, _('iOS')),
        (OTHER, _('Other')),
    )

    branding_information = models.ForeignKey(BrandingInformation)
    client_id = models.CharField(max_length=255)
    uri = models.CharField(max_length=255)
    redirect_uri = models.CharField(max_length=255)
    java_script_origins = models.CharField(max_length=255)
    app_type = models.CharField(max_length=1,
                                choices=APP_TYPE_CHOICES)
    installed_app_type = models.CharField(max_length=1,
                                          choices=INSTALLED_APP_TYPE_CHOICES)
    enable_deep_link = models.BooleanField(default=False)

    # Android
    package_name = models.CharField(max_length=255)
    fingerprint = models.CharField(max_length=255)

    # Chrome
    app_id = models.CharField(max_length=255)

    # iOS
    bundle_id = models.CharField(max_length=255)
    app_store_id = models.CharField(max_length=255)
