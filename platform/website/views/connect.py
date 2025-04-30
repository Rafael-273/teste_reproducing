from django.views.generic import TemplateView


class ConnectView(TemplateView):
    template_name = 'front/connect.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar_start_color'] = 'var(--primary-color)'
        context['navbar_scroll_color'] = 'var(--primary-color)'
        return context
