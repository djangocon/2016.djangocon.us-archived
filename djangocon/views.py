from django.views.generic.detail import DetailView

from symposion.sponsorship.models import Sponsor


class SponsorView(DetailView):

    model = Sponsor
    template_name = 'symposion/sponsorship/sponsor_public_detail.html'
