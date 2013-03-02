from __future__ import absolute_import, unicode_literals

from django import forms

from .models import BrandingInformation, ClientIdentifier


class BrandingInformationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BrandingInformationForm, self).__init__(*args, **kwargs)
        self.fields['account'].widget = forms.HiddenInput()

    class Meta:
        model = BrandingInformation


class ClientIdentifierForm(forms.ModelForm):
    def __init__(self, branding, *args, **kwargs):
        super(ClientIdentifierForm, self).__init__(*args, **kwargs)
        self.fields['branding_information'].widget = forms.HiddenInput()
        self.fields['branding_information'].initial = branding.id

    class Meta:
        model = ClientIdentifier
