from django.urls import path

from .views import AdultCreateView, TeamSelectView

urlpatterns = [
    path("", TeamSelectView.as_view(), name="team-select"),
    path("adult/", AdultCreateView.as_view(), name="adult-new"),
]
