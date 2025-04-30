from django.urls import path
from .views.home import HomeView
from .views.engage import CoachingView, ChurchPlanterPathwayView, ExistingChurchPathwayView, MarketplaceLeaderPathwayView, ConsultingView, ConferenceView, CareView
from .views.collaborate import CollaborateView
from .views.donate import DonateView
from .views.connect import ConnectView
from .views.about import AboutView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('coaching/', CoachingView.as_view(), name='coaching'),
    path('church_planter_pathway/', ChurchPlanterPathwayView.as_view(), name='church_planter_pathway'),
    path('existing_church_pathway/', ExistingChurchPathwayView.as_view(), name='existing_church_pathway'),
    path('marketplace_leader_pathway/', MarketplaceLeaderPathwayView.as_view(), name='marketplace_leader_pathway'),
    path('consulting/', ConsultingView.as_view(), name='consulting'),
    path('conferences/', ConferenceView.as_view(), name='conferences'),
    path('care/', CareView.as_view(), name='care'),
    path('collaborate/', CollaborateView.as_view(), name='collaborate'),
    path('donate/', DonateView.as_view(), name='donate'),
    path('connect/', ConnectView.as_view(), name='connect'),
    path('about/', AboutView.as_view(), name='about'),
]