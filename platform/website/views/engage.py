from django.views.generic import TemplateView


class ChurchPlanterPathwayView(TemplateView):
    template_name = 'front/church_planter_pathway.html'


class ExistingChurchPathwayView(TemplateView):
    template_name = 'front/existing_church_pathway.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar_scroll_color'] = '#6FD6A9'
        return context


class MarketplaceLeaderPathwayView(TemplateView):
    template_name = 'front/marketplace_leader_pathway.html'


class CoachingView(TemplateView):
    template_name = 'front/coaching.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar_scroll_color'] = '#6FD6A9'
        return context


class ConsultingView(TemplateView):
    template_name = 'front/consulting.html'


class ConferenceView(TemplateView):
    template_name = 'front/conferences.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar_scroll_color'] = '#6FD6A9'
        return context


class CareView(TemplateView):
    template_name = 'front/care.html'


