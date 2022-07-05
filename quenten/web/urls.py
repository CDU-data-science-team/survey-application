from django.urls import path

from .views import (
    PersonCreateView,
    PersonUpdateView,
    ResultsListView,
    TeamSelectView,
    UncodedListView,
    UncodedUpdateNext,
    UncodedUpdateView,
)

urlpatterns = [
    path("", TeamSelectView.as_view(), name="team-select"),
    path("adult/", PersonCreateView.as_view(), name="adult-new"),
    path("child/", PersonCreateView.as_view(), name="child-new"),
    path("youngcarer/", PersonCreateView.as_view(), name="young-carer-new"),
    path("carer/", PersonCreateView.as_view(), name="carer-new"),
    path("accessible/", PersonCreateView.as_view(), name="accessible-new"),
    path("results/", ResultsListView.as_view(), name="results"),
    path("results/<uuid:uuid>", PersonUpdateView.as_view(), name="result-detail"),
    path(
        "results/<uuid:uuid>/update", PersonUpdateView.as_view(), name="result-update"
    ),
    path("uncoded", UncodedListView.as_view(), name="uncoded-list"),
    path("uncoded/<uuid:uuid>", UncodedUpdateView.as_view(), name="uncoded-update"),
    path("uncoded/next", UncodedUpdateNext.as_view(), name="uncoded-next"),
]
