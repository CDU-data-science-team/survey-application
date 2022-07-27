import django_filters
from web import forms, models


class ResultFilter(django_filters.FilterSet):
    """
    Filter for use on the responses list view.
    """

    _PERSONS = [
        ("adult", "Adult"),
        ("child", "Child / Young Person"),
        ("carer", "Carer"),
        ("youngcarer", "Young Carer"),
        ("accessible", "Accessible"),
    ]
    paper_index = django_filters.CharFilter(
        field_name="paper_index", lookup_expr="icontains"
    )
    team__name = django_filters.CharFilter(
        field_name="team__name", lookup_expr="icontains"
    )
    form_type = django_filters.ChoiceFilter(
        method="form_type_filter", choices=_PERSONS, label="Form type"
    )

    class Meta:
        model = models.Person
        form = forms.PersonFilterForm
        fields = ["paper_index", "team__name", "added_by"]

    def form_type_filter(self, queryset, value, *args, **kwargs):
        """
        Filter based on the form_type options
        """
        form_arg = args[0]
        try:
            if form_arg == "adult":
                queryset = queryset.filter(adult__isnull=False)
            if form_arg == "child":
                queryset = queryset.filter(child__isnull=False)
            if form_arg == "carer":
                queryset = queryset.filter(carer__isnull=False)
            if form_arg == "youngcarer":
                queryset = queryset.filter(youngcarer__isnull=False)
            if form_arg == "accessible":
                queryset = queryset.filter(accessible__isnull=False)
        except ValueError:
            pass
        return queryset
