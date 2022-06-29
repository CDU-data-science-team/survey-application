from typing import Any, Dict

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.shortcuts import HttpResponseRedirect, redirect
from django.views.generic import CreateView, FormView, ListView, UpdateView

from .forms import AdultForm, TeamForm
from .models import Accessible, Adult, Carer, Child, Person, Team, YoungCarer


class TeamSelectView(LoginRequiredMixin, FormView):
    """
    Form view for selecting the team and redirecting on form choice.
    """

    form_class = TeamForm
    template_name = "forms/team_form.html"

    def form_valid(self, form: TeamForm) -> HttpResponseRedirect:
        """
        Override to pass data to the next form.
        """
        self.form = form
        team = form.cleaned_data["team"].id
        self.request.session["team"] = str(team)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self) -> str:
        """
        Override to redirect to the users chosen form.
        """
        user_choice = self.form.cleaned_data["choice"]
        self.success_url = f"/{user_choice}"
        return super().get_success_url()


class AdultCreateView(LoginRequiredMixin, CreateView):
    """
    Form view to create adult form response.
    Further forms can follow this template.
    """

    model = Adult
    form_class = AdultForm
    template_name = "forms/person_form.html"
    success_url = "/"

    def get_form_kwargs(self) -> Dict[str, Any]:
        """
        Override to add additional request parameters for form and team.
        """
        kwargs = super(AdultCreateView, self).get_form_kwargs()
        kwargs["request"] = self.request

        team_id = self.request.session.get("team")
        if team_id is not None:
            team_object = Team.objects.filter(id=team_id).first()
            kwargs["team"] = team_object
            self.extra_context = {
                "name": team_object.name,
                "address": team_object.district,
            }
        return kwargs


class AdultUpdateView(LoginRequiredMixin, UpdateView):
    """
    Update view.
    """

    model = Adult
    form_class = AdultForm
    template_name: str = "forms/person_form.html"
    success_url = "/"

    def get_object(self) -> Adult:
        return Adult.objects.get(id=self.kwargs.get("uuid"))

    def get_form_kwargs(self) -> Dict[str, Any]:
        """
        Override to add additional request parameters for form and team.
        """
        kwargs = super(AdultUpdateView, self).get_form_kwargs()
        kwargs["request"] = self.request

        team_object = self.object.team
        kwargs["team"] = self.object.team
        self.extra_context = {"name": team_object.name, "address": team_object.district}
        return kwargs


class ResultsListView(LoginRequiredMixin, ListView):
    """
    List view for all survey results.
    """

    template_name: str = "list.html"
    model: Person

    def get_queryset(self) -> QuerySet:
        """
        Override.
        """
        return Person.objects.order_by("-created_at")
