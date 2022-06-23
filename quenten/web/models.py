import uuid

from django.db import models
from users.models import CustomUser


class Gender(models.TextChoices):
    MALE = "M", "Male"
    FEMALE = "F", "Female"
    OTHER = "O", "Other"
    REFUSED = "R", "Refused"


class EthnicGroup(models.TextChoices):
    BRITISH = "BG", "British"
    IRISH = "IR", "Irish"
    CARIBBEAN = "CA", "Caribbean"
    AFRICAN = "AF", "African"
    INDIAN = "IN", "Indian"
    PAKISTANI = "PA", "Pakistani"
    BANGLADESHI = "BA", "Bangladeshi"
    W_B_CARIBBEAN = "WBC", "White and Black Caribbean"
    W_B_AFRICAN = "WBA", "White and Black African"
    W_ASIAN = "WA", "White African"
    CHINESE = "CH", "Chinese"
    GRT = "GRT", "Gypsy/Roma/Traveller"
    DO_NOT_WISH_TO_SAY = "DNWTS", "Do not wish to say"
    REFUSED = "R", "Refused"


class Disability(models.TextChoices):
    YES = "Y", "Yes"
    NO = "N", "No"
    DO_NOT_WISH_TO_SAY = "DNWTS", "Do not wish to say"
    REFUSED = "R", "Refused"


class Religion(models.TextChoices):
    CHRISTIAN = "C", "Christian"
    BUDDHIST = "B", "Buddhist"
    HINDU = "H", "Hindu"
    JEWISH = "J", "Jewish"
    MUSLIM = "M", "Muslim"
    SIKH = "S", "Sikh"
    NO_RELIGION = "NR", "No religion"
    DO_NOT_WISH_TO_SAY = "DNWTS", "Do not wish to say"
    REFUSED = "R", "Refused"


class SexualOrientation(models.TextChoices):
    HETEROSEXUAL = "H", "Heterosexual"
    GAY_MAN = "G", "Gay man"
    LESBIAN = "L", "Lesbian"
    BISEXUAL = "B", "Bisexual"
    PANSEXUAL = "P", "Pansexual"
    DEMISEXUAL = "D", "Demisexual"
    DO_NOT_WISH_TO_SAY = "DNWTS", "Do not wish to say"
    REFUSED = "R", "Refused"


class Age(models.TextChoices):
    U12 = "U12", "Under 12"
    _12_17 = "12", " 12-17"
    _18_25 = "18", " 18-25"
    _26_39 = "26", " 26-39"
    _40_64 = "40", " 40-64"
    _65_79 = "65", " 65-79"
    _80 = "80", " 80+"
    REFUSED = "R", "Refused"


class Relationship(models.TextChoices):
    SINGLE = "S", "Single"
    CIVIL_PARTNERSHIP = "CP", "Civil Partnership"
    WIDOWED = "W", "Widowed"
    MARRIED = "M", "Married"
    SEPARATED = "SP", "Separated"
    CO_HABITING = "CH", "Co-habiting"
    DIVORCED = "D", "Divorced"
    DO_NOT_WISH_TO_SAY = "DNWTS", "Do not wish to say"
    REFUSED = "R", "Refused"


class Pregnancy(models.TextChoices):
    YES = "Y", "Yes"
    NO = "N", "No"
    DO_NOT_WISH_TO_SAY = "DNWTS", "Do not wish to say"
    REFUSED = "R", "Refused"


class Rating(models.TextChoices):
    VERY_GOOD = "5", "Very good"
    GOOD = "4", "Good"
    NEITHER = "3", "Neither good nor poor"
    POOR = "2", "Poor"
    VERY_POOR = "1", "Very poor"
    DONT_KNOW = "0", "Don't know"


class ServiceUser(models.TextChoices):
    PATIENT = "PATIENT", "Patient/Service User"
    CARER = "CARER", "Carer/Relative/Friend"


class BaseModel(models.Model):
    """
    Base model for all models
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class DemographicsMixin(models.Model):
    """
    Mixin for demographic fields.
    """

    class Meta:
        abstract = True

    gender = models.CharField(max_length=5, choices=Gender.choices)
    ethnic_group = models.CharField(max_length=5, choices=EthnicGroup.choices)
    disability = models.CharField(max_length=5, choices=Disability.choices)
    religion = models.CharField(max_length=5, choices=Religion.choices)
    sexual_orientation = models.CharField(
        max_length=5, choices=SexualOrientation.choices
    )
    ages = models.CharField(max_length=3, choices=Age.choices)
    relationship = models.CharField(max_length=5, choices=Relationship.choices)


class PregnancyMixin(models.Model):
    """
    Mixin for pregnancy fields.
    """

    class Meta:
        abstract = True

    pregnant = models.CharField(max_length=5, choices=Pregnancy.choices)
    baby = models.CharField(max_length=5, choices=Pregnancy.choices)


class Directorate(BaseModel):
    """
    Mirroring existing fields for now.
    """

    name = models.CharField(max_length=128)
    code = models.IntegerField()


class Team(BaseModel):
    """
    Mirroring existing fields for now.
    """

    directorate = models.ForeignKey(Directorate, on_delete=models.CASCADE)
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


class Person(BaseModel):
    """
    Base class for all forms.
    """

    class Meta:
        abstract = True

    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    added_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, editable=False)
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


class Adult(Person, DemographicsMixin, PregnancyMixin):
    """
    Adult survey form.
    """

    class Meta:
        pass

    carer_type = models.CharField(
        max_length=7, choices=ServiceUser.choices, help_text="I am a: "
    )
    experience = models.CharField(
        max_length=1,
        choices=Rating.choices,
        help_text="Overall, how was your experience of our service?",
    )
    listening = models.CharField(
        max_length=1,
        choices=Rating.choices,
        help_text="How good were our services at listening to you?",
    )
    explaining = models.CharField(
        max_length=1,
        choices=Rating.choices,
        help_text="How good were our services at explaining information clearly?",
    )
    kind = models.CharField(
        max_length=1,
        choices=Rating.choices,
        help_text="How good were our services at being kind to you?",
    )
    treatment = models.CharField(
        max_length=1,
        choices=Rating.choices,
        help_text="How good were our services at involving you in decisions about your care or treatment?",
    )
    positive = models.CharField(
        max_length=1,
        choices=Rating.choices,
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
