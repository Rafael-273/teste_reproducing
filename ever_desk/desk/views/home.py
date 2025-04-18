from django.views.generic import ListView

class HomeView(ListView):
    template_name = 'front/home.html'