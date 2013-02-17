from django import forms

from .models import BrandingInformation, ClientID


class BrandingInformationForm(forms.ModelForm):

    class Meta:
        model = BrandingInformation


class ClientIDForm(forms.ModelForm):

    class Meta:
        model = ClientID
