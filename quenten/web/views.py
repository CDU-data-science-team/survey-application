from typing import Any, Dict

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import HttpResponseRedirect
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    FormView,
    ListView,
    UpdateView,
)

from .forms import AdultForm, TeamForm
from .models import Accessible, Adult, Carer, Child, Team, YoungCarer


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
    template_name = "forms/adult_form.html"
    success_url = "/"

    def get_form_kwargs(self) -> Dict[str, Any]:
        """
        Override to add additional request parameters for form and team.
        """
        kwargs = super(AdultCreateView, self).get_form_kwargs()
        kwargs["request"] = self.request

        team_id = self.request.session["team"]
        team_object = Team.objects.filter(id=team_id).first()
        kwargs["team"] = team_object
        self.extra_context = {"name": team_object.name, "address": team_object.district}
        return kwargs
