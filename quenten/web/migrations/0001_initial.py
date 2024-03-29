# Generated by Django 4.0.5 on 2022-06-27 14:11

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Age",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=128)),
                ("value", models.CharField(max_length=128)),
                ("sort_order", models.PositiveIntegerField()),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Directorate",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=128)),
                ("code", models.IntegerField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Disability",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=128)),
                ("value", models.CharField(max_length=128)),
                ("sort_order", models.PositiveIntegerField()),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="EthnicGroup",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=128)),
                ("value", models.CharField(max_length=128)),
                ("sort_order", models.PositiveIntegerField()),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Gender",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=128)),
                ("value", models.CharField(max_length=128)),
                ("sort_order", models.PositiveIntegerField()),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Person",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "comments_good",
                    models.TextField(blank=True, help_text="What was good?", null=True),
                ),
                (
                    "comments_better",
                    models.TextField(
                        blank=True, help_text="What could we do better?", null=True
                    ),
                ),
                (
                    "comments_public",
                    models.BooleanField(
                        blank=True,
                        help_text="Please tick here if you DO NOT wish your comments to be made public",
                        null=True,
                    ),
                ),
                (
                    "added_by",
                    models.ForeignKey(
                        editable=False,
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Pregnant",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=128)),
                ("value", models.CharField(max_length=128)),
                ("sort_order", models.PositiveIntegerField()),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Rating",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=128)),
                ("value", models.CharField(max_length=128)),
                ("sort_order", models.PositiveIntegerField()),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Relationship",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=128)),
                ("value", models.CharField(max_length=128)),
                ("sort_order", models.PositiveIntegerField()),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Religion",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=128)),
                ("value", models.CharField(max_length=128)),
                ("sort_order", models.PositiveIntegerField()),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ServiceUser",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=128)),
                ("value", models.CharField(max_length=128)),
                ("sort_order", models.PositiveIntegerField()),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="SexualOrientation",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=128)),
                ("value", models.CharField(max_length=128)),
                ("sort_order", models.PositiveIntegerField()),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Accessible",
            fields=[
                (
                    "person_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="web.person",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("web.person",),
        ),
        migrations.CreateModel(
            name="Carer",
            fields=[
                (
                    "person_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="web.person",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("web.person",),
        ),
        migrations.CreateModel(
            name="Child",
            fields=[
                (
                    "person_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="web.person",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("web.person",),
        ),
        migrations.CreateModel(
            name="YoungCarer",
            fields=[
                (
                    "person_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="web.person",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("web.person",),
        ),
        migrations.CreateModel(
            name="Team",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=128)),
                ("code", models.DecimalField(decimal_places=3, max_digits=10)),
                ("date_from", models.DateField()),
                ("date_to", models.DateField()),
                ("time", models.IntegerField(blank=True, null=True)),
                ("division", models.IntegerField(blank=True, null=True)),
                ("contacts", models.IntegerField(blank=True, null=True)),
                ("his", models.CharField(blank=True, max_length=100, null=True)),
                ("inpatient", models.IntegerField(blank=True, null=True)),
                ("district", models.CharField(blank=True, max_length=40, null=True)),
                (
                    "sub_district",
                    models.CharField(blank=True, max_length=40, null=True),
                ),
                (
                    "fft_category",
                    models.CharField(blank=True, max_length=60, null=True),
                ),
                (
                    "directorate",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="web.directorate",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="person",
            name="team",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="web.team"
            ),
        ),
        migrations.CreateModel(
            name="Adult",
            fields=[
                (
                    "person_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="web.person",
                    ),
                ),
                (
                    "age",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="web.age"
                    ),
                ),
                (
                    "baby",
                    models.ForeignKey(
                        help_text="Have you had a baby within the last 26 weeks?",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="baby",
                        to="web.pregnant",
                    ),
                ),
                (
                    "carer_type",
                    models.ForeignKey(
                        help_text="I am a: ",
                        on_delete=django.db.models.deletion.PROTECT,
                        to="web.serviceuser",
                    ),
                ),
                (
                    "disability",
                    models.ForeignKey(
                        help_text="Do you have a long term disability or a long-term health condition which affects your day to day activities?",
                        on_delete=django.db.models.deletion.PROTECT,
                        to="web.disability",
                    ),
                ),
                (
                    "ethnic_group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="web.ethnicgroup",
                    ),
                ),
                (
                    "experience",
                    models.ForeignKey(
                        help_text="Overall, how was your experience of our service?",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="experience",
                        to="web.rating",
                    ),
                ),
                (
                    "explaining",
                    models.ForeignKey(
                        help_text="How good were our services at explaining information clearly?",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="explaining",
                        to="web.rating",
                    ),
                ),
                (
                    "gender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="web.gender"
                    ),
                ),
                (
                    "kind",
                    models.ForeignKey(
                        help_text="How good were our services at being kind to you?",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="kind",
                        to="web.rating",
                    ),
                ),
                (
                    "listening",
                    models.ForeignKey(
                        help_text="How good were our services at listening to you?",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="listening",
                        to="web.rating",
                    ),
                ),
                (
                    "positive",
                    models.ForeignKey(
                        help_text="How good were our services at making a positive difference to your health and wellbeing?",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="positive",
                        to="web.rating",
                    ),
                ),
                (
                    "pregnant",
                    models.ForeignKey(
                        help_text="Are you pregnant at this time?",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="pregnant",
                        to="web.pregnant",
                    ),
                ),
                (
                    "relationship",
                    models.ForeignKey(
                        help_text="What is your relationship status?",
                        on_delete=django.db.models.deletion.PROTECT,
                        to="web.relationship",
                    ),
                ),
                (
                    "religion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="web.religion"
                    ),
                ),
                (
                    "sexual_orientation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="web.sexualorientation",
                    ),
                ),
                (
                    "treatment",
                    models.ForeignKey(
                        help_text="How good were our services at involving you in decisions about your care or treatment?",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="treatment",
                        to="web.rating",
                    ),
                ),
            ],
            bases=("web.person", models.Model),
        ),
    ]
