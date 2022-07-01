from django.urls import path

from .views import (
    AdultCreateView,
    AdultUpdateView,
    ResultsListView,
    TeamSelectView,
    UncodedListView,
    UncodedUpdateNext,
    UncodedUpdateView,
)

urlpatterns = [
    path("", TeamSelectView.as_view(), name="team-select"),
    path("adult/", AdultCreateView.as_view(), name="adult-new"),
    path("results/", ResultsListView.as_view(), name="results"),
    path("results/<uuid:uuid>", AdultUpdateView.as_view(), name="result-detail"),
    path("results/<uuid:uuid>/update", AdultUpdateView.as_view(), name="result-update"),
    path("uncoded", UncodedListView.as_view(), name="uncoded-list"),
    path("uncoded/<uuid:uuid>", UncodedUpdateView.as_view(), name="uncoded-update"),
    path("uncoded/next", UncodedUpdateNext.as_view(), name="uncoded-next"),
]
