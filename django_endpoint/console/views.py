from django.views.generic import ListView

from braces.views import LoginRequiredMixin


from .models import BrandingInformation, ClientID


class BrandingInformationList(ListView):
    model = BrandingInformation


class ConsoleHomeList(LoginRequiredMixin, ListView):
    template_name = 'console/console_home.html'
    model = ClientID

    def get_context_data(self, **kwargs):
        context = super(ConsoleHomeList, self).get_context_data(**kwargs)
        context['branding_information'] = BrandingInformation.objects.filter(
            user=self.request.user)
        return context
