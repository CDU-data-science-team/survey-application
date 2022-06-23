# forms.py
from typing import Any

from crispy_forms.helper import FormHelper
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
            "ages",
            "relationship",
            "pregnant",
            "baby",
        )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        self.team_object = kwargs.pop("team")

        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"

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
