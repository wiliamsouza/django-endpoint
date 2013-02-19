from __future__ import absolute_import, unicode_literals

from django import forms

from .models import BrandingInformation, ClientIdentifier


class BrandingInformationForm(forms.ModelForm):

    class Meta:
        model = BrandingInformation


class ClientIdentifierForm(forms.ModelForm):

    class Meta:
        model = ClientIdentifier
