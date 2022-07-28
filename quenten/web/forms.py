# forms.py
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Div, Field, Layout, Submit
from django import forms

from .models import Accessible, Adult, Carer, Child, Person, YoungCarer


class PersonSelectForm(forms.Form):
    """
    Initial form to select the response type.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Div(
                Submit("form-choice", "Adult Form", css_class="mt-3"),
            ),
            Div(
                Submit("form-choice", "Young Person Form", css_class="mt-3"),
            ),
            Div(
                Submit("form-choice", "Carer Form", css_class="mt-3"),
            ),
            Div(
                Submit("form-choice", "Young Carer Form", css_class="mt-3"),
            ),
            Div(
                Submit("form-choice", "Accessible Form", css_class="mt-3"),
            ),
        )


class PersonFilterForm(forms.Form):
    """
    Form for filtering on the ListViews
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "get"
        self.helper.layout = Layout(
            Div(
                Field(
                    "paper_index",
                    wrapper_class="col-md-2",
                    css_class="form-control",
                ),
                Field(
                    "team__name",
                    wrapper_class="col-md-2",
                    css_class="form-control",
                ),
                Field(
                    "added_by",
                    wrapper_class="col-md-2",
                    css_class="form-control",
                ),
                Field(
                    "form_type",
                    wrapper_class="col-md-2",
                    css_class="form-control",
                ),
                css_class="row",
            ),
            Submit("submit", "Filter", css_class="mt-3 mb-3"),
        )


class CodingLayout(Layout):
    """
    Form layout for the comments coding of responses.
    Added to forms if the user has permissions.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(
            HTML('<hr class="mt-4">'),
            HTML('<h6 class="mt-4">Comments Coding</h6>'),
            Div(
                Field(
                    "best_code_1",
                    wrapper_class="col-md-4",
                    rows="2",
                    css_class="form-control",
                ),
                Field(
                    "best_code_2",
                    wrapper_class="col-md-4",
                    css_class="form-control",
                ),
                Field(
                    "positivity",
                    wrapper_class="col-md-4",
                    css_class="form-control",
                ),
                css_class="row mb-3",
            ),
            Div(
                Field(
                    "improve_code_1",
                    wrapper_class="col-md-4",
                    css_class="form-control",
                ),
                Field(
                    "improve_code_2",
                    wrapper_class="col-md-4",
                    css_class="form-control",
                ),
                Field(
                    "criticality",
                    wrapper_class="col-md-4",
                    css_class="form-control",
                ),
                css_class="row mb-3",
            ),
        )


class PersonForm(forms.ModelForm):
    """
    Base form for all person forms.
    """

    class Meta:
        model = Person
        exclude = ()

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", "")

        super().__init__(*args, **kwargs)
        self.helper = self.get_form_helper()

        if self.request.user.has_perm("web.code_response"):
            self.helper.layout.append(CodingLayout())

    def get_form_helper(self) -> FormHelper:
        """
        Builds the form helper configuration
        """
        helper = FormHelper()
        helper.form_method = "post"
        helper.form_tag = False
        helper.layout = self.get_form_layout()
        return helper

    def get_form_layout(self) -> Layout:
        """
        Override to explicitly build the form layout
        """
        layout = Layout(
            Div(
                Field(
                    "team",
                    wrapper_class="col-md-4",
                    css_class="form-control",
                    autofocus="autofocus",
                ),
                css_class="row",
            ),
        )
        return layout


class AdultForm(PersonForm):
    class Meta:
        model = Adult
        exclude = ()

    def get_form_layout(self) -> Layout:
        layout = super().get_form_layout()
        layout.append(
            Layout(
                Div(
                    Field(
                        "carer_type",
                        wrapper_class="col-md-4",
                        css_class="form-control",
                    ),
                    css_class="row",
                ),
                Div(
                    Field(
                        "experience",
                        wrapper_class="col-md-4",
                        css_class="form-control",
                    ),
                    Field(
                        "listening",
                        wrapper_class="col-md-4",
                        css_class="form-control",
                    ),
                    Field(
                        "explaining",
                        wrapper_class="col-md-4",
                        css_class="form-control",
                    ),
                    css_class="row",
                ),
                Div(
                    Field(
                        "kind",
                        wrapper_class="col-md-4",
                        css_class="form-control",
                    ),
                    Field(
                        "treatment",
                        wrapper_class="col-md-4",
                        css_class="form-control",
                    ),
                    Field(
                        "positive",
                        wrapper_class="col-md-4",
                        css_class="form-control",
                    ),
                    css_class="row",
                ),
                Div(
                    Field(
                        "comments_good",
                        wrapper_class="col-md-6",
                        rows="3",
                        css_class="form-control",
                    ),
                    Field(
                        "comments_better",
                        wrapper_class="col-md-6",
                        rows="3",
                        css_class="form-control",
                    ),
                    css_class="row",
                ),
                Field(
                    "comments_public",
                    wrapper_class="col-md-4",
                    css_class="form-control",
                ),
                Div(
                    Field("gender", wrapper_class="col-md-4", css_class="form-control"),
                    Field(
                        "ethnic_group",
                        wrapper_class="col-md-4",
                        css_class="form-control",
                    ),
                    Field(
                        "disability", wrapper_class="col-md-4", css_class="form-control"
                    ),
                    css_class="row",
                ),
                Div(
                    Field(
                        "religion", wrapper_class="col-md-4", css_class="form-control"
                    ),
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
                        "relationship",
                        wrapper_class="col-md-4",
                        css_class="form-control",
                    ),
                    Field(
                        "pregnant", wrapper_class="col-md-4", css_class="form-control"
                    ),
                    Field("baby", wrapper_class="col-md-4", css_class="form-control"),
                    css_class="row",
                ),
            )
        )
        return layout


class ChildForm(PersonForm):
    class Meta:
        model = Child
        exclude = ()

    def get_form_layout(self) -> Layout:
        layout = super().get_form_layout()
        layout.append(
            Layout(
                Div(
                    Field(
                        "carer_type",
                        wrapper_class="col-md-4",
                        css_class="form-control",
                    ),
                    css_class="row",
                ),
                Div(
                    Field(
                        "experience", wrapper_class="col-md-4", css_class="form-control"
                    ),
                    Field(
                        "listening", wrapper_class="col-md-4", css_class="form-control"
                    ),
                    Field(
                        "explaining", wrapper_class="col-md-4", css_class="form-control"
                    ),
                    css_class="row",
                ),
                Div(
                    Field("kind", wrapper_class="col-md-4", css_class="form-control"),
                    Field(
                        "treatment", wrapper_class="col-md-4", css_class="form-control"
                    ),
                    Field(
                        "positive", wrapper_class="col-md-4", css_class="form-control"
                    ),
                    css_class="row",
                ),
                Div(
                    Field(
                        "comments_good",
                        wrapper_class="col-md-6",
                        rows="3",
                        css_class="form-control",
                    ),
                    Field(
                        "comments_better",
                        wrapper_class="col-md-6",
                        rows="3",
                        css_class="form-control",
                    ),
                    css_class="row",
                ),
                Field(
                    "comments_public",
                    wrapper_class="col-md-4",
                    css_class="form-control",
                ),
                Div(
                    Field("gender", wrapper_class="col-md-4", css_class="form-control"),
                    Field(
                        "ethnic_group",
                        wrapper_class="col-md-4",
                        css_class="form-control",
                    ),
                    Field(
                        "disability", wrapper_class="col-md-4", css_class="form-control"
                    ),
                    css_class="row",
                ),
                Div(
                    Field(
                        "religion", wrapper_class="col-md-4", css_class="form-control"
                    ),
                    Field("age", wrapper_class="col-md-4", css_class="form-control"),
                    css_class="row",
                ),
            )
        )
        return layout


class YoungCarerForm(PersonForm):
    class Meta:
        model = YoungCarer
        exclude = ()

    def get_form_layout(self) -> Layout:
        layout = super().get_form_layout()
        layout.append(
            Layout(
                Div(
                    Field(
                        "experience",
                        wrapper_class="col-md-4",
                        css_class="form-control",
                    ),
                    Field(
                        "listening", wrapper_class="col-md-4", css_class="form-control"
                    ),
                    Field(
                        "explaining", wrapper_class="col-md-4", css_class="form-control"
                    ),
                    css_class="row",
                ),
                Div(
                    Field("kind", wrapper_class="col-md-4", css_class="form-control"),
                    Field(
                        "involving", wrapper_class="col-md-4", css_class="form-control"
                    ),
                    Field(
                        "talking", wrapper_class="col-md-4", css_class="form-control"
                    ),
                    css_class="row",
                ),
                Div(
                    Field(
                        "worried", wrapper_class="col-md-4", css_class="form-control"
                    ),
                    Field(
                        "assessment", wrapper_class="col-md-4", css_class="form-control"
                    ),
                    css_class="row",
                ),
                Div(
                    Field(
                        "comments_good",
                        wrapper_class="col-md-6",
                        rows="3",
                        css_class="form-control",
                    ),
                    Field(
                        "comments_better",
                        wrapper_class="col-md-6",
                        rows="3",
                        css_class="form-control",
                    ),
                    css_class="row",
                ),
                Field(
                    "comments_public",
                    wrapper_class="col-md-4",
                    css_class="form-control",
                ),
                Div(
                    Field("gender", wrapper_class="col-md-4", css_class="form-control"),
                    Field(
                        "ethnic_group",
                        wrapper_class="col-md-4",
                        css_class="form-control",
                    ),
                    Field(
                        "disability", wrapper_class="col-md-4", css_class="form-control"
                    ),
                    css_class="row",
                ),
                Div(
                    Field(
                        "religion", wrapper_class="col-md-4", css_class="form-control"
                    ),
                    Field("age", wrapper_class="col-md-4", css_class="form-control"),
                    css_class="row",
                ),
            )
        )
        return layout


class CarerForm(PersonForm):
    class Meta:
        model = Carer
        exclude = ()

    def get_form_layout(self) -> Layout:
        layout = super().get_form_layout()
        layout.append(
            Layout(
                Div(
                    Field(
                        "experience",
                        wrapper_class="col-md-4",
                        css_class="form-control",
                    ),
                    Field(
                        "listening", wrapper_class="col-md-4", css_class="form-control"
                    ),
                    Field(
                        "explaining", wrapper_class="col-md-4", css_class="form-control"
                    ),
                    css_class="row",
                ),
                Div(
                    Field("kind", wrapper_class="col-md-4", css_class="form-control"),
                    Field(
                        "treatment", wrapper_class="col-md-4", css_class="form-control"
                    ),
                    Field(
                        "support", wrapper_class="col-md-4", css_class="form-control"
                    ),
                    css_class="row",
                ),
                Div(
                    Field(
                        "worried", wrapper_class="col-md-4", css_class="form-control"
                    ),
                    Field(
                        "assessment", wrapper_class="col-md-4", css_class="form-control"
                    ),
                    css_class="row",
                ),
                Div(
                    Field(
                        "comments_good",
                        wrapper_class="col-md-6",
                        rows="3",
                        css_class="form-control",
                    ),
                    Field(
                        "comments_better",
                        wrapper_class="col-md-6",
                        rows="3",
                        css_class="form-control",
                    ),
                    css_class="row",
                ),
                Field(
                    "comments_public",
                    wrapper_class="col-md-4",
                    css_class="form-control",
                ),
                Div(
                    Field("gender", wrapper_class="col-md-4", css_class="form-control"),
                    Field(
                        "ethnic_group",
                        wrapper_class="col-md-4",
                        css_class="form-control",
                    ),
                    Field(
                        "disability", wrapper_class="col-md-4", css_class="form-control"
                    ),
                    css_class="row",
                ),
                Div(
                    Field(
                        "religion", wrapper_class="col-md-4", css_class="form-control"
                    ),
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
                        "relationship",
                        wrapper_class="col-md-4",
                        css_class="form-control",
                    ),
                    Field(
                        "carer_type", wrapper_class="col-md-4", css_class="form-control"
                    ),
                    css_class="row",
                ),
            )
        )
        return layout


class AccessibleForm(PersonForm):
    class Meta:
        model = Accessible
        exclude = ()

    def get_form_layout(self) -> Layout:
        layout = super().get_form_layout()
        layout.append(
            Layout(
                Div(
                    Field(
                        "carer_type",
                        wrapper_class="col-md-4",
                        css_class="form-control",
                    ),
                    css_class="row",
                ),
                Div(
                    Field(
                        "experience", wrapper_class="col-md-4", css_class="form-control"
                    ),
                    Field(
                        "listening", wrapper_class="col-md-4", css_class="form-control"
                    ),
                    Field(
                        "explaining", wrapper_class="col-md-4", css_class="form-control"
                    ),
                    css_class="row",
                ),
                Div(
                    Field("kind", wrapper_class="col-md-4", css_class="form-control"),
                    Field("ask", wrapper_class="col-md-4", css_class="form-control"),
                    Field("better", wrapper_class="col-md-4", css_class="form-control"),
                    css_class="row",
                ),
                Div(
                    Field(
                        "comments_good",
                        wrapper_class="col-md-6",
                        rows="3",
                        css_class="form-control",
                    ),
                    Field(
                        "comments_better",
                        wrapper_class="col-md-6",
                        rows="3",
                        css_class="form-control",
                    ),
                    css_class="row",
                ),
            )
        )
        return layout


class CodeForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = (
            "comments_good",
            "best_code_1",
            "best_code_2",
            "positivity",
            "comments_better",
            "improve_code_1",
            "improve_code_2",
            "criticality",
            "comments_public",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Div(
                Field(
                    "comments_good",
                    readonly=True,
                    wrapper_class="col-md-9",
                    rows="4",
                    css_class="form-control",
                ),
                css_class="row mb-3",
            ),
            Div(
                Field(
                    "comments_better",
                    readonly=True,
                    wrapper_class="col-md-9",
                    rows="4",
                    css_class="form-control",
                ),
                css_class="row mb-3",
            ),
            CodingLayout(),
            Submit("submit", "Save and next form"),
            Submit("submit-back", "Save and back to list"),
        )
