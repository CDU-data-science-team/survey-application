from django.urls import path

from .views import (
    PersonCreateView,
    PersonSelectView,
    PersonUpdateView,
    ResultsListView,
    UncodedListView,
    UncodedUpdateNext,
    UncodedUpdateView,
)

urlpatterns = [
    path("", PersonSelectView.as_view(), name="person-select"),
    path("adult/", PersonCreateView.as_view(), name="adult-new"),
    path("child/", PersonCreateView.as_view(), name="child-new"),
    path("youngcarer/", PersonCreateView.as_view(), name="young-carer-new"),
    path("carer/", PersonCreateView.as_view(), name="carer-new"),
    path("accessible/", PersonCreateView.as_view(), name="accessible-new"),
    path("results/", ResultsListView.as_view(), name="results"),
    path("results/<int:paper_index>", PersonUpdateView.as_view(), name="result-detail"),
    path(
        "results/<int:paper_index>/update",
        PersonUpdateView.as_view(),
        name="result-update",
    ),
    path("uncoded", UncodedListView.as_view(), name="uncoded-list"),
    path(
        "uncoded/<int:paper_index>", UncodedUpdateView.as_view(), name="uncoded-update"
    ),
    path("uncoded/next", UncodedUpdateNext.as_view(), name="uncoded-next"),
]
