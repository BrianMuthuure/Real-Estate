from django.urls import path
from .views import GetProfileAPIView, \
    AgentListAPIView, UpdateProfileAPIView, \
    TopAgentsListAPIView

urlpatterns = [
    path("me/", GetProfileAPIView.as_view(), name='get_profile'),
    path("update/<str:username>/", UpdateProfileAPIView.as_view(), name='update_profile'),
    path("agents/all/", AgentListAPIView.as_view(), name='all_agents'),
    path("top-agents/all/", TopAgentsListAPIView.as_view(), name='top-agents')
]
