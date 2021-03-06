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
        context = super(ConsoleHomeList, self).get_context_data(**kwargs)
        user = self.request.user
        branding_info, created = BrandingInformation.objects.get_or_create(
            account=user)
        branding_form = BrandingInformationForm(instance=branding_info)
        context['branding_information'] = branding_info
        context['branding_information_form'] = branding_form
        context['client_identifier_form'] = ClientIdentifierForm(branding_info)
        return context


class BrandingInformationUpdate(LoginRequiredMixin, UpdateView):
    model = BrandingInformation
    success_url = reverse_lazy('console_home')


class ClientIdentifierCreate(LoginRequiredMixin, CreateView):
    model = ClientIdentifier
    success_url = reverse_lazy('console_home')


class ClientIdentifierUpdate(LoginRequiredMixin, UpdateView):
    model = ClientIdentifier
    success_url = reverse_lazy('console_home')
