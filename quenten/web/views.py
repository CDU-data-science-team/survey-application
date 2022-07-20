from typing import Any, Dict

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.db.models.query import QuerySet
from django.forms import Form
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, ListView, UpdateView

from .forms import (
    AccessibleForm,
    AdultForm,
    CarerForm,
    ChildForm,
    CodeForm,
    PersonSelectForm,
    YoungCarerForm,
)
from .models import Accessible, Adult, Carer, Child, Person, YoungCarer


class PersonSelectView(LoginRequiredMixin, FormView):
    """
    Form view for selecting and redirecting on the form choice.
    """

    form_class = PersonSelectForm
    template_name = "forms/team_form.html"

    def form_valid(self, form: PersonSelectForm) -> HttpResponseRedirect:
        """
        Override to pass data to the next form.
        """
        self.form = form
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self) -> str:
        """
        Override to redirect to the users chosen form.
        """
        user_choice = self.form.cleaned_data["choice"]
        self.success_url = f"/{user_choice}"
        return super().get_success_url()


class PersonCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
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
        elif url_name == "young-carer-new":
            self.model = YoungCarer
            self.form_class = YoungCarerForm
        elif url_name == "carer-new":
            self.model = Carer
            self.form_class = CarerForm
        elif url_name == "accessible-new":
            self.model = Accessible
            self.form_class = AccessibleForm

        return super().setup(request, *args, **kwargs)

    def form_valid(self, form: Any) -> HttpResponse:
        form.instance.added_by = self.request.user
        return super().form_valid(form)

    def get_success_message(self, cleaned_data: Dict[str, str]) -> str:
        return f"Submission successful. Paper index is: {self.object.paper_index}"


class PersonUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Update view.
    """

    model = Person
    form_class = None
    template_name: str = "forms/person_form.html"
    success_url = "/results/"

    def get_object(self) -> Person:
        return Person.objects.get_subclass(paper_index=self.kwargs.get("paper_index"))

    def get_form_class(self) -> Form:
        if type(self.object) == Adult:
            self.form_class = AdultForm
        if type(self.object) == Child:
            self.form_class = ChildForm
        if type(self.object) == YoungCarer:
            self.form_class = YoungCarerForm
        if type(self.object) == Carer:
            self.form_class = CarerForm
        if type(self.object) == Accessible:
            self.form_class = AccessibleForm
        return super().get_form_class()

    def form_valid(self, form: AdultForm) -> HttpResponse:
        form.instance.added_by = self.request.user
        return super().form_valid(form)

    def get_success_message(self, cleaned_data: Dict[str, str]) -> str:
        return f"Update successful. Paper index is: {self.object.paper_index}"


class ResultsListView(LoginRequiredMixin, ListView):
    """
    List view for all survey results.
    """

    template_name: str = "list.html"
    model: Person
    paginate_by = 20

    def get_queryset(self) -> QuerySet:
        """
        Override.
        """
        return (
            Person.objects.select_subclasses(
                Adult, Child, YoungCarer, Carer, Accessible
            )
            .prefetch_related("team", "added_by")
            .order_by("-created_at")
        )


class UncodedListView(LoginRequiredMixin, ListView):
    """
    List view for uncoded results.
    """

    template_name: str = "uncoded_list.html"
    model: Person
    paginate_by = 20

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
        return (
            q.select_subclasses()
            .prefetch_related("team", "added_by")
            .order_by("-created_at")
        )


class UncodedUpdateView(LoginRequiredMixin, UpdateView):
    """
    Update view for a specific uncoded result.
    """

    model = Person
    form_class = CodeForm
    template_name: str = "forms/person_form.html"

    def get_object(self) -> Person:
        return Person.objects.get(paper_index=self.kwargs.get("paper_index"))

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
