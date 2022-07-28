import uuid

from django.db import models
from django.urls import reverse
from model_utils.managers import InheritanceManager
from users.models import CustomUser


class BaseModel(models.Model):
    """
    Base model for all models
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class FormResponses(models.Model):
    """
    Forms model for response types.
    Used for filtering question responses.
    """

    form_choices = [
        ("adult", "Adult"),
        ("child", "Child"),
        ("carer", "Carer"),
        ("young carer", "Young Carer"),
        ("accessible", "Accessible"),
    ]
    name = models.CharField(max_length=20, choices=form_choices, unique=True)

    def __str__(self) -> str:
        return f"{self.name}"


class QuestionOption(BaseModel):
    """
    Base model for all responses.
    """

    name = models.CharField(max_length=128)
    value = models.CharField(max_length=128)
    sort_order = models.PositiveIntegerField()
    hidden = models.BooleanField(
        default=False, help_text="Select if the field needs to be hidden on the form"
    )
    forms = models.ManyToManyField(
        FormResponses,
        help_text="Select which forms the response should be displayed on",
        blank=True,
    )

    class Meta:
        abstract = True
        ordering = ["sort_order"]

    def __str__(self) -> str:
        return f"{self.name}"


class Gender(QuestionOption):
    pass


class EthnicGroup(QuestionOption):
    pass


class Disability(QuestionOption):
    pass


class Religion(QuestionOption):
    pass


class SexualOrientation(QuestionOption):
    pass


class Age(QuestionOption):
    pass


class Relationship(QuestionOption):
    pass


class Pregnant(QuestionOption):
    pass


class ServiceUser(QuestionOption):
    pass


class Rating(QuestionOption):
    pass


class CommentsCode(QuestionOption):
    pass


class ContactGeneric(QuestionOption):
    pass


class CarerType(QuestionOption):
    pass


class DemographicsMixin(models.Model):
    """
    Mixin for demographic fields.
    """

    class Meta:
        abstract = True

    gender = models.ForeignKey(
        Gender,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        limit_choices_to={"hidden": False},
    )
    ethnic_group = models.ForeignKey(
        EthnicGroup,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        limit_choices_to={"hidden": False},
    )
    disability = models.ForeignKey(
        Disability,
        on_delete=models.PROTECT,
        help_text="Do you have a long term disability or a long-term health condition which affects your day to day activities?",
        blank=True,
        null=True,
        limit_choices_to={"hidden": False},
    )
    religion = models.ForeignKey(
        Religion,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        limit_choices_to={"hidden": False},
    )
    sexual_orientation = models.ForeignKey(
        SexualOrientation,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        limit_choices_to={"hidden": False},
    )
    age = models.ForeignKey(
        Age,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        limit_choices_to={"hidden": False},
    )
    relationship = models.ForeignKey(
        Relationship,
        on_delete=models.PROTECT,
        help_text="What is your relationship status?",
        blank=True,
        null=True,
        limit_choices_to={"hidden": False},
    )


class PregnancyMixin(models.Model):
    """
    Mixin for pregnancy fields.
    """

    form_name = "Pregnancy"

    class Meta:
        abstract = True

    pregnant = models.ForeignKey(
        Pregnant,
        related_name="pregnant",
        on_delete=models.PROTECT,
        help_text="Are you pregnant at this time?",
        blank=True,
        null=True,
        limit_choices_to={"hidden": False},
    )
    baby = models.ForeignKey(
        Pregnant,
        related_name="baby",
        on_delete=models.PROTECT,
        help_text="Have you had a baby within the last 26 weeks?",
        blank=True,
        null=True,
        limit_choices_to={"hidden": False},
    )


class Directorate(BaseModel):
    """
    Mirroring existing fields for now.
    """

    name = models.CharField(max_length=128)
    code = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.name}"


class Team(BaseModel):
    """
    Mirroring existing fields for now.
    """

    directorate = models.ForeignKey(Directorate, on_delete=models.PROTECT)
    name = models.CharField(max_length=128)
    code = models.DecimalField(max_digits=7, decimal_places=3)
    date_from = models.DateField()
    date_to = models.DateField()
    time = models.IntegerField(null=True, blank=True)
    division = models.IntegerField(null=True, blank=True)
    contacts = models.IntegerField(null=True, blank=True)
    his = models.CharField(max_length=100, null=True, blank=True)
    inpatient = models.IntegerField(null=True, blank=True)
    district = models.CharField(max_length=40, null=True, blank=True)
    sub_district = models.CharField(max_length=40, null=True, blank=True)
    fft_category = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.code}, {self.name}, {self.directorate}"


class Person(BaseModel):
    """
    Base class for all forms.
    """

    form_name = "Person"

    class Meta:

        ordering = ["updated_at"]
        permissions = [
            ("add_response", "Can add new form responses"),
            ("update_response", "Can update form responses"),
            ("code_response", "Can code forms based on comments"),
        ]

    objects = InheritanceManager()

    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    added_by = models.ForeignKey(CustomUser, on_delete=models.PROTECT, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    paper_index = models.IntegerField(editable=False, null=True, unique=True)

    comments_good = models.TextField(null=True, blank=True, help_text="What was good?")
    best_code_1 = models.ForeignKey(
        CommentsCode,
        related_name="best1",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    best_code_2 = models.ForeignKey(
        CommentsCode,
        related_name="best2",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    positivity = models.PositiveIntegerField(null=True, blank=True)

    comments_better = models.TextField(
        null=True, blank=True, help_text="What could we do better?"
    )
    improve_code_1 = models.ForeignKey(
        CommentsCode,
        related_name="improve1",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    improve_code_2 = models.ForeignKey(
        CommentsCode,
        related_name="improve2",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    criticality = models.PositiveIntegerField(null=True, blank=True)

    comments_public = models.BooleanField(
        null=True,
        blank=True,
        help_text="Please tick here if you DO NOT wish your comments to be made public",
    )

    @property
    def is_coded(self) -> bool:
        """
        Returns false if the response needs to be coded.
        A response needs coding if it has comments in comments_good or comments_better
        And the codes best_code_1/2 improve_code_1/2 are blank
        """
        if not self.comments_better and not self.comments_good:
            return True
        if (
            not self.best_code_1
            or not self.best_code_2
            or not self.improve_code_1
            or not self.improve_code_2
        ):
            return False
        return True

    def __str__(self) -> str:
        return f"{self.paper_index}"

    def get_absolute_url(self):
        return reverse("result-detail", self.paper_index)

    def save(self, *args, **kwargs) -> None:
        """
        Override to set the paper_index from created_at and increment it.
        """
        super().save(*args, **kwargs)

        if not self.paper_index:
            quarter = (self.created_at.month + 2) // 3
            increment = (
                Person._base_manager.filter(
                    created_at__year=self.created_at.year,
                    created_at__quarter=quarter,
                    created_at__lt=self.created_at,
                ).count()
                + 1
            )
            self.paper_index = int(f"{self.created_at.year}{quarter}{increment}")

        return super().save(*args, **kwargs)


class Adult(Person, DemographicsMixin, PregnancyMixin):
    """
    Adult survey form.
    """

    form_name = "Adult"

    class Meta:
        pass

    carer_type = models.ForeignKey(
        ServiceUser,
        on_delete=models.PROTECT,
        help_text="I am a: ",
        blank=True,
        null=True,
        limit_choices_to={"hidden": False, "forms__name": form_name},
    )
    experience = models.ForeignKey(
        Rating,
        related_name="experience",
        on_delete=models.PROTECT,
        help_text="Overall, how was your experience of our service?",
        blank=True,
        null=True,
        limit_choices_to={"hidden": False, "forms__name": form_name},
    )
    listening = models.ForeignKey(
        Rating,
        related_name="listening",
        on_delete=models.PROTECT,
        help_text="How good were our services at listening to you?",
        blank=True,
        null=True,
        limit_choices_to={"hidden": False, "forms__name": form_name},
    )
    explaining = models.ForeignKey(
        Rating,
        related_name="explaining",
        on_delete=models.PROTECT,
        help_text="How good were our services at explaining information clearly?",
        blank=True,
        null=True,
        limit_choices_to={"hidden": False, "forms__name": form_name},
    )
    kind = models.ForeignKey(
        Rating,
        related_name="kind",
        on_delete=models.PROTECT,
        help_text="How good were our services at being kind to you?",
        blank=True,
        null=True,
        limit_choices_to={"hidden": False, "forms__name": form_name},
    )
    treatment = models.ForeignKey(
        Rating,
        related_name="treatment",
        on_delete=models.PROTECT,
        help_text="How good were our services at involving you in decisions about your care or treatment?",
        blank=True,
        null=True,
        limit_choices_to={"hidden": False, "forms__name": form_name},
    )
    positive = models.ForeignKey(
        Rating,
        related_name="positive",
        on_delete=models.PROTECT,
        help_text="How good were our services at making a positive difference to your health and wellbeing?",
        blank=True,
        null=True,
        limit_choices_to={"hidden": False, "forms__name": form_name},
    )
    age = models.ForeignKey(
        Age,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        limit_choices_to={"hidden": False, "forms__name": form_name},
    )


class Child(Person, DemographicsMixin):
    """
    Child survey form.
    """

    form_name = "Child"

    class Meta:
        pass

    carer_type = models.ForeignKey(
        ServiceUser,
        on_delete=models.PROTECT,
        help_text="I am a: ",
        blank=True,
        null=True,
        limit_choices_to={"hidden": False, "forms__name": form_name},
    )
    experience = models.ForeignKey(
        Rating,
        related_name="child_experience",
        on_delete=models.PROTECT,
        help_text="Overall, how was your experience of our service?",
        blank=True,
        null=True,
        limit_choices_to={"hidden": False, "forms__name": form_name},
    )
    listening = models.ForeignKey(
        Rating,
        related_name="child_listening",
        on_delete=models.PROTECT,
        help_text="How good were our services at listening to you?",
        blank=True,
        null=True,
        limit_choices_to={"hidden": False, "forms__name": form_name},
    )
    explaining = models.ForeignKey(
        Rating,
        related_name="child_explaining",
        on_delete=models.PROTECT,
        help_text="How good were our services at explaining information clearly?",
        blank=True,
        null=True,
        limit_choices_to={"hidden": False, "forms__name": form_name},
    )
    kind = models.ForeignKey(
        Rating,
        related_name="child_kind",
        on_delete=models.PROTECT,
        help_text="How good were our services at being kind to you?",
        blank=True,
        null=True,
        limit_choices_to={"hidden": False, "forms__name": form_name},
    )
    treatment = models.ForeignKey(
        Rating,
        related_name="child_treatment",
        on_delete=models.PROTECT,
        help_text="How good were our services at involving you in decisions about your care or treatment?",
        blank=True,
        null=True,
        limit_choices_to={"hidden": False, "forms__name": form_name},
    )
    positive = models.ForeignKey(
        Rating,
        related_name="child_positive",
        on_delete=models.PROTECT,
        help_text="How good were our services at making a positive difference to your health and wellbeing?",
        blank=True,
        null=True,
        limit_choices_to={"hidden": False, "forms__name": form_name},
    )
    age = models.ForeignKey(
        Age,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        limit_choices_to={"hidden": False, "forms__name": form_name},
    )


class Carer(Person, DemographicsMixin):
    """
    Carer survey form.
    """

    form_name = "Carer"

    class Meta:
        pass

    experience = models.ForeignKey(
        Rating,
        related_name="carer_experience",
        on_delete=models.PROTECT,
        help_text="Overall, how was your experience of our service?",
        blank=True,
        null=True,
        limit_choices_to={"hidden": False, "forms__name": form_name},
    )
    listening = models.ForeignKey(
        Rating,
        related_name="carer_listening",
        on_delete=models.PROTECT,
        help_text="How good were our services at listening to you?",
        blank=True,
        null=True,
        limit_choices_to={"hidden": False, "forms__name": form_name},
    )
    explaining = models.ForeignKey(
        Rating,
        related_name="carer_explaining",
        on_delete=models.PROTECT,
        help_text="How good were our services at explaining information clearly?",
        blank=True,
        null=True,
        limit_choices_to={"hidden": False, "forms__name": form_name},
    )
    kind = models.ForeignKey(
        Rating,
        related_name="carer_kind",
        on_delete=models.PROTECT,
        help_text="How good were our services at being kind to you?",
        blank=True,
        null=True,
        limit_choices_to={"hidden": False, "forms__name": form_name},
    )
    treatment = models.ForeignKey(
        Rating,
        related_name="carer_treatment",
        on_delete=models.PROTECT,
        help_text="How good were our services at involving you in decisions about the care and treatment of the person you care for?",
        blank=True,
        null=True,
        limit_choices_to={"hidden": False, "forms__name": form_name},
    )
    support = models.ForeignKey(
        Rating,
        related_name="carer_support",
        on_delete=models.PROTECT,
        help_text="How good were our services at giving you information about support for you as a carer?",
        blank=True,
        null=True,
        limit_choices_to={"hidden": False, "forms__name": form_name},
    )
    worried = models.ForeignKey(
        ContactGeneric,
        related_name="carer_worried",
        on_delete=models.PROTECT,
        help_text="Did our services tell you who you could contact if you were worried about the person you care for?",
        blank=True,
        null=True,
        limit_choices_to={"hidden": False, "forms__name": form_name},
    )
    assessment = models.ForeignKey(
        ContactGeneric,
        related_name="carer_assessment",
        on_delete=models.PROTECT,
        help_text="Did we tell you who to contact for a carers assessment?",
        blank=True,
        null=True,
        limit_choices_to={"hidden": False, "forms__name": form_name},
    )
    carer_type = models.ForeignKey(
        CarerType,
        related_name="carer_type",
        on_delete=models.PROTECT,
        help_text="I am a carer, family member, friend, parent or guardian of someone:",
        blank=True,
        null=True,
        limit_choices_to={"hidden": False, "forms__name": form_name},
    )


class YoungCarer(Person, DemographicsMixin):
    """
    Young carer survey form.
    """

    form_name = "Young Carer"

    class Meta:
        pass

    experience = models.ForeignKey(
        Rating,
        related_name="young_carer_experience",
        on_delete=models.PROTECT,
        help_text="Overall, how was your experience of our service?",
        blank=True,
        null=True,
        limit_choices_to={"hidden": False, "forms__name": form_name},
    )
    listening = models.ForeignKey(
        Rating,
        related_name="young_carer_listening",
        on_delete=models.PROTECT,
        help_text="Were our services good at listening to you?",
        blank=True,
        null=True,
        limit_choices_to={"hidden": False, "forms__name": form_name},
    )
    explaining = models.ForeignKey(
        Rating,
        related_name="young_carer_explaining",
        on_delete=models.PROTECT,
        help_text="Were our services good at explaining things clearly?",
        blank=True,
        null=True,
        limit_choices_to={"hidden": False, "forms__name": form_name},
    )
    kind = models.ForeignKey(
        Rating,
        related_name="young_carer_kind",
        on_delete=models.PROTECT,
        help_text="Were our services good at being kind to you?",
        blank=True,
        null=True,
        limit_choices_to={"hidden": False, "forms__name": form_name},
    )
    involving = models.ForeignKey(
        Rating,
        related_name="young_carer_involving",
        on_delete=models.PROTECT,
        help_text="Were our services good at involving you in the way we helped the person you care for?",
        blank=True,
        null=True,
        limit_choices_to={"hidden": False, "forms__name": form_name},
    )
    talking = models.ForeignKey(
        Rating,
        related_name="young_carer_talking",
        on_delete=models.PROTECT,
        help_text="Were our services good at talking to you about the support you could have as a carer?",
        blank=True,
        null=True,
        limit_choices_to={"hidden": False, "forms__name": form_name},
    )
    worried = models.ForeignKey(
        Rating,
        related_name="young_carer_worried",
        on_delete=models.PROTECT,
        help_text="Did our services tell you who you could contact if you were worried about the person you care for?",
        blank=True,
        null=True,
        limit_choices_to={"hidden": False, "forms__name": form_name},
    )
    assessment = models.ForeignKey(
        Rating,
        related_name="young_carer_assessment",
        on_delete=models.PROTECT,
        help_text="Did we tell you who to contact for a carers assessment?",
        blank=True,
        null=True,
        limit_choices_to={"hidden": False, "forms__name": form_name},
    )
    age = models.ForeignKey(
        Age,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        limit_choices_to={"hidden": False, "forms__name": form_name},
    )


class Accessible(Person):
    """
    Accessible survey form.
    """

    form_name = "Accessible"

    class Meta:
        pass

    carer_type = models.ForeignKey(
        ServiceUser,
        on_delete=models.PROTECT,
        help_text="I am a: ",
        blank=True,
        null=True,
        limit_choices_to={"hidden": False, "forms__name": form_name},
    )
    experience = models.ForeignKey(
        Rating,
        related_name="accessible_experience",
        on_delete=models.PROTECT,
        help_text="Did you have a good experience from our staff?",
        blank=True,
        null=True,
        limit_choices_to={"hidden": False, "forms__name": form_name},
    )
    listening = models.ForeignKey(
        Rating,
        related_name="accessible_listening",
        on_delete=models.PROTECT,
        help_text="Did our staff listen to you?",
        blank=True,
        null=True,
        limit_choices_to={"hidden": False, "forms__name": form_name},
    )
    explaining = models.ForeignKey(
        Rating,
        related_name="accessible_explaining",
        on_delete=models.PROTECT,
        help_text="Did our staff explain things clearly?",
        blank=True,
        null=True,
        limit_choices_to={"hidden": False, "forms__name": form_name},
    )
    kind = models.ForeignKey(
        Rating,
        related_name="accessible_kind",
        on_delete=models.PROTECT,
        help_text="Were our staff kind to you?",
        blank=True,
        null=True,
        limit_choices_to={"hidden": False, "forms__name": form_name},
    )
    ask = models.ForeignKey(
        Rating,
        related_name="accessible_ask",
        on_delete=models.PROTECT,
        help_text="Did our staff ask you what you wanted?",
        blank=True,
        null=True,
        limit_choices_to={"hidden": False, "forms__name": form_name},
    )
    better = models.ForeignKey(
        Rating,
        related_name="accessible_better",
        on_delete=models.PROTECT,
        help_text="Did our staff help you feel better?",
        blank=True,
        null=True,
        limit_choices_to={"hidden": False, "forms__name": form_name},
    )
