from typing import Any, Dict, Optional

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.db.models.query import QuerySet
from django.forms import Form
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, ListView, UpdateView

from .forms import AdultForm, ChildForm, CodeForm, TeamForm
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


class PersonCreateView(LoginRequiredMixin, CreateView):
    """
    Form view to create adult form response.
    Further forms can follow this template.
    """

    model = None
    form_class = None
    template_name = "forms/person_form.html"
    success_url = "/"

    def setup(self, request: HttpRequest, *args: Any, **kwargs: Any) -> None:
        """
        Override to set the model and form based on the url name.
        """
        url_name = request.resolver_match.url_name

        if url_name == "adult-new":
            self.model = Adult
            self.form_class = AdultForm

        elif url_name == "child-new":
            self.model = Child
            self.form_class = ChildForm

        return super().setup(request, *args, **kwargs)

    def get_form_kwargs(self) -> Dict[str, Any]:
        """
        Override to add additional request parameters for form and team.
        """
        kwargs = super(PersonCreateView, self).get_form_kwargs()
        kwargs["request"] = self.request

        team_id = self.request.session.get("team")
        if team_id is not None:
            team_object = Team.objects.filter(id=team_id).first()
            kwargs["team"] = team_object
            self.extra_context = {
                "code": team_object.code,
                "name": team_object.name,
                "directorate": team_object.directorate,
            }
        return kwargs


class PersonUpdateView(LoginRequiredMixin, UpdateView):
    """
    Update view.
    """

    model = Person
    form_class = None
    template_name: str = "forms/person_form.html"
    success_url = "/"

    def get_object(self) -> Person:
        return Person.objects.get_subclass(id=self.kwargs.get("uuid"))

    def get_form_class(self) -> Form:
        if type(self.object) == Adult:
            self.form_class = AdultForm
        if type(self.object) == Child:
            self.form_class = ChildForm
        return super().get_form_class()

    def get_form_kwargs(self) -> Dict[str, Any]:
        """
        Override to add additional request parameters for form and team.
        """
        kwargs = super(PersonUpdateView, self).get_form_kwargs()
        kwargs["request"] = self.request

        team_object = self.object.team
        kwargs["team"] = self.object.team
        self.extra_context = {
            "code": team_object.code,
            "name": team_object.name,
            "directorate": team_object.directorate,
        }
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
        return Person.objects.select_subclasses(Adult, Child).order_by("-created_at")


class UncodedListView(LoginRequiredMixin, ListView):
    """
    List view for uncoded results.
    """

    template_name: str = "uncoded_list.html"
    model: Person

    def get_queryset(self) -> QuerySet:
        """
        Override - filter on if response has comments and is uncoded.
        """
        q = Person.objects
        q = q.filter(~Q(comments_good="") | ~Q(comments_better=""))
        q = q.filter(
            (
                Q(best_code_1__isnull=True)
                | Q(best_code_2__isnull=True)
                | Q(improve_code_1__isnull=True)
                | Q(improve_code_2__isnull=True)
            )
        )
        return q.order_by("-created_at")


class UncodedUpdateView(LoginRequiredMixin, UpdateView):
    """
    Update view for a specific uncoded result.
    """

    model = Person
    form_class = CodeForm
    template_name: str = "forms/person_form.html"

    def get_object(self) -> Person:
        return Person.objects.get(id=self.kwargs.get("uuid"))

    def get_form_kwargs(self) -> Dict[str, Any]:
        """
        Override to add additional request parameters for form and team.
        """
        kwargs = super(UncodedUpdateView, self).get_form_kwargs()
        kwargs["request"] = self.request

        team_object = self.object.team
        kwargs["team"] = self.object.team
        self.extra_context = {"name": team_object.name, "address": team_object.district}
        return kwargs

    def get_success_url(self) -> str:
        return (
            reverse_lazy("uncoded-list")
            if "submit-back" in self.request.POST
            else reverse_lazy("uncoded-next")
        )


class UncodedUpdateNext(UncodedUpdateView):
    """
    Update view for the next uncoded result.
    """

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        self.object = self.get_object()
        if self.object is None:
            return redirect(reverse_lazy("uncoded-list"))
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_object(self) -> Person:
        q = Person.objects
        q = q.filter(~Q(comments_good="") | ~Q(comments_better=""))
        q = q.filter(
            (
                Q(best_code_1__isnull=True)
                | Q(best_code_2__isnull=True)
                | Q(improve_code_1__isnull=True)
                | Q(improve_code_2__isnull=True)
            )
        ).first()
        return q
