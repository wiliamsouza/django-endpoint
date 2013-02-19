from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from braces.views import LoginRequiredMixin

from .models import BrandingInformation, ClientIdentifier
from .forms import BrandingInformationForm, ClientIdentifierForm


class ConsoleHomeList(LoginRequiredMixin, ListView):
    template_name = 'console/console_home.html'
    model = ClientIdentifier

    def get_context_data(self, **kwargs):
        branding_information = None
        context = super(ConsoleHomeList, self).get_context_data(**kwargs)
        try:
            branding_information = self.request.user.brandinginformation
        except BrandingInformation.DoesNotExist:
            branding_information = None
        context['branding_information'] = branding_information
        context['branding_information_form'] = BrandingInformationForm()
        context['client_identifier_form'] = ClientIdentifierForm()
        return context


class BrandingInformationCreate(LoginRequiredMixin, CreateView):
    model = BrandingInformation
    success_url = reverse_lazy('console_home')


class BrandingInformationUpdate(LoginRequiredMixin, UpdateView):
    model = BrandingInformation
    success_url = reverse_lazy('console_home')


class ClientIdentifierCreate(LoginRequiredMixin, CreateView):
    model = ClientIdentifier
    success_url = reverse_lazy('console_home')


class ClientIdentifierUpdate(LoginRequiredMixin, UpdateView):
    model = ClientIdentifier
    success_url = reverse_lazy('console_home')
