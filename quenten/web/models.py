import uuid

from django.db import models
from users.models import CustomUser


class BaseModel(models.Model):
    """
    Base model for all models
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class QuestionOption(BaseModel):
    """
    Base model for all responses.
    """

    name = models.CharField(max_length=128)
    value = models.CharField(max_length=128)
    sort_order = models.PositiveIntegerField()

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


class DemographicsMixin(models.Model):
    """
    Mixin for demographic fields.
    """

    class Meta:
        abstract = True

    gender = models.ForeignKey(Gender, on_delete=models.PROTECT)
    ethnic_group = models.ForeignKey(EthnicGroup, on_delete=models.PROTECT)
    disability = models.ForeignKey(
        Disability,
        on_delete=models.PROTECT,
        help_text="Do you have a long term disability or a long-term health condition which affects your day to day activities?",
    )
    religion = models.ForeignKey(Religion, on_delete=models.PROTECT)
    sexual_orientation = models.ForeignKey(SexualOrientation, on_delete=models.PROTECT)
    age = models.ForeignKey(Age, on_delete=models.PROTECT)
    relationship = models.ForeignKey(
        Relationship,
        on_delete=models.PROTECT,
        help_text="What is your relationship status?",
    )


class PregnancyMixin(models.Model):
    """
    Mixin for pregnancy fields.
    """

    class Meta:
        abstract = True

    pregnant = models.ForeignKey(
        Pregnant,
        related_name="pregnant",
        on_delete=models.PROTECT,
        help_text="Are you pregnant at this time?",
    )
    baby = models.ForeignKey(
        Pregnant,
        related_name="baby",
        on_delete=models.PROTECT,
        help_text="Have you had a baby within the last 26 weeks?",
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
    code = models.DecimalField(max_digits=3, decimal_places=3)
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
        return f"{self.code}, {self.name}, {self.district}"


class Person(BaseModel):
    """
    Base class for all forms.
    """

    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    added_by = models.ForeignKey(CustomUser, on_delete=models.PROTECT, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    comments_good = models.TextField(null=True, blank=True, help_text="What was good?")
    comments_better = models.TextField(
        null=True, blank=True, help_text="What could we do better?"
    )
    comments_public = models.BooleanField(
        null=True,
        blank=True,
        help_text="Please tick here if you DO NOT wish your comments to be made public",
    )

    def __str__(self) -> str:
        return f"{self.created_at}, {self.team.name}"


class Adult(Person, DemographicsMixin, PregnancyMixin):
    """
    Adult survey form.
    """

    class Meta:
        pass

    carer_type = models.ForeignKey(
        ServiceUser, on_delete=models.PROTECT, help_text="I am a: "
    )
    experience = models.ForeignKey(
        Rating,
        related_name="experience",
        on_delete=models.PROTECT,
        help_text="Overall, how was your experience of our service?",
    )
    listening = models.ForeignKey(
        Rating,
        related_name="listening",
        on_delete=models.PROTECT,
        help_text="How good were our services at listening to you?",
    )
    explaining = models.ForeignKey(
        Rating,
        related_name="explaining",
        on_delete=models.PROTECT,
        help_text="How good were our services at explaining information clearly?",
    )
    kind = models.ForeignKey(
        Rating,
        related_name="kind",
        on_delete=models.PROTECT,
        help_text="How good were our services at being kind to you?",
    )
    treatment = models.ForeignKey(
        Rating,
        related_name="treatment",
        on_delete=models.PROTECT,
        help_text="How good were our services at involving you in decisions about your care or treatment?",
    )
    positive = models.ForeignKey(
        Rating,
        related_name="positive",
        on_delete=models.PROTECT,
        help_text="How good were our services at making a positive difference to your health and wellbeing?",
    )


class Child(Person):
    """
    Child survey form.
    """

    pass


class Carer(Person):
    """
    Carer survey form.
    """

    pass


class YoungCarer(Person):
    """
    Young carer survey form.
    """

    pass


class Accessible(Person):
    """
    Accessible survey form.
    """

    pass
