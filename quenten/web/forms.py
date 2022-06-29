# forms.py
from typing import Any

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Field, Layout, Submit
from django import forms

from .models import Adult, Team


class TeamForm(forms.Form):
    """
    Form to select team and post data.
    """

    _FORMS = [
        ("adult", "Adult Form"),
        ("young", "Young Form"),
        ("carers", "Carers Form"),
        ("youngcarers", "Young Carers Form"),
        ("accessible", "Accessible Form"),
    ]
    teams = Team.objects.all()
    team = forms.ModelChoiceField(
        queryset=teams, widget=forms.Select(attrs={"autofocus": "autofocus"})
    )
    choice = forms.ChoiceField(choices=_FORMS, widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Field(
                "team",
                wrapper_class="col-md-4",
                css_class="form-control",
                autofocus="autofocus",
            ),
            Field("choice", wrapper_class="col-md-4", css_class="form-control"),
            Submit("submit", "Submit", css_class="mt-3"),
        )


class AdultForm(forms.ModelForm):
    class Meta:
        model = Adult
        fields = (
            "carer_type",
            "experience",
            "listening",
            "explaining",
            "kind",
            "treatment",
            "positive",
            "comments_good",
            "comments_better",
            "comments_public",
            "gender",
            "ethnic_group",
            "disability",
            "religion",
            "sexual_orientation",
            "age",
            "relationship",
            "pregnant",
            "baby",
        )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        self.team_object = kwargs.pop("team", "")

        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Div(
                Field(
                    "carer_type",
                    wrapper_class="col-md-4",
                    css_class="form-control",
                    autofocus="autofocus",
                ),
                css_class="row",
            ),
            Div(
                Field("experience", wrapper_class="col-md-4", css_class="form-control"),
                Field("listening", wrapper_class="col-md-4", css_class="form-control"),
                Field("explaining", wrapper_class="col-md-4", css_class="form-control"),
                css_class="row",
            ),
            Div(
                Field("kind", wrapper_class="col-md-4", css_class="form-control"),
                Field("treatment", wrapper_class="col-md-4", css_class="form-control"),
                Field("positive", wrapper_class="col-md-4", css_class="form-control"),
                css_class="row",
            ),
            Div(
                Field(
                    "comments_good",
                    wrapper_class="col-md-6",
                    rows="2",
                    css_class="form-control",
                ),
                Field(
                    "comments_better",
                    wrapper_class="col-md-6",
                    rows="2",
                    css_class="form-control",
                ),
                css_class="row",
            ),
            Field(
                "comments_public", wrapper_class="col-md-4", css_class="form-control"
            ),
            Div(
                Field("gender", wrapper_class="col-md-4", css_class="form-control"),
                Field(
                    "ethnic_group", wrapper_class="col-md-4", css_class="form-control"
                ),
                Field("disability", wrapper_class="col-md-4", css_class="form-control"),
                css_class="row",
            ),
            Div(
                Field("religion", wrapper_class="col-md-4", css_class="form-control"),
                Field(
                    "sexual_orientation",
                    wrapper_class="col-md-4",
                    css_class="form-control",
                ),
                Field("age", wrapper_class="col-md-4", css_class="form-control"),
                css_class="row",
            ),
            Div(
                Field(
                    "relationship", wrapper_class="col-md-4", css_class="form-control"
                ),
                Field("pregnant", wrapper_class="col-md-4", css_class="form-control"),
                Field("baby", wrapper_class="col-md-4", css_class="form-control"),
                css_class="row",
            ),
            Submit("submit", "Submit", css_class="mt-3"),
        )

    def save(self, commit=True) -> Any:
        """
        Override to add hidden fields
        """
        instance = super().save(commit=False)
        instance.added_by = self.request.user
        instance.team = self.team_object

        if commit:
            instance.save()
        return instance