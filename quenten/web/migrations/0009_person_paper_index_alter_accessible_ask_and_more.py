# Generated by Django 4.0.5 on 2022-07-20 10:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0008_age_hidden_carertype_hidden_childage_hidden_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="person",
            name="paper_index",
            field=models.IntegerField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name="accessible",
            name="ask",
            field=models.ForeignKey(
                blank=True,
                help_text="Did our staff ask you what you wanted?",
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="accessible_ask",
                to="web.childrating",
            ),
        ),
        migrations.AlterField(
            model_name="accessible",
            name="better",
            field=models.ForeignKey(
                blank=True,
                help_text="Did our staff help you feel better?",
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="accessible_better",
                to="web.childrating",
            ),
        ),
        migrations.AlterField(
            model_name="accessible",
            name="carer_type",
            field=models.ForeignKey(
                blank=True,
                help_text="I am a: ",
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="web.serviceuser",
            ),
        ),
        migrations.AlterField(
            model_name="accessible",
            name="experience",
            field=models.ForeignKey(
                blank=True,
                help_text="Did you have a good experience from our staff?",
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="accessible_experience",
                to="web.childrating",
            ),
        ),
        migrations.AlterField(
            model_name="accessible",
            name="explaining",
            field=models.ForeignKey(
                blank=True,
                help_text="Did our staff explain things clearly?",
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="accessible_explaining",
                to="web.childrating",
            ),
        ),
        migrations.AlterField(
            model_name="accessible",
            name="kind",
            field=models.ForeignKey(
                blank=True,
                help_text="Were our staff kind to you?",
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="accessible_kind",
                to="web.childrating",
            ),
        ),
        migrations.AlterField(
            model_name="accessible",
            name="listening",
            field=models.ForeignKey(
                blank=True,
                help_text="Did our staff listen to you?",
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="accessible_listening",
                to="web.childrating",
            ),
        ),
        migrations.AlterField(
            model_name="adult",
            name="age",
            field=models.ForeignKey(
                blank=True,
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="web.age",
            ),
        ),
        migrations.AlterField(
            model_name="adult",
            name="baby",
            field=models.ForeignKey(
                blank=True,
                help_text="Have you had a baby within the last 26 weeks?",
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="baby",
                to="web.pregnant",
            ),
        ),
        migrations.AlterField(
            model_name="adult",
            name="carer_type",
            field=models.ForeignKey(
                blank=True,
                help_text="I am a: ",
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="web.serviceuser",
            ),
        ),
        migrations.AlterField(
            model_name="adult",
            name="disability",
            field=models.ForeignKey(
                blank=True,
                help_text="Do you have a long term disability or a long-term health condition which affects your day to day activities?",
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="web.disability",
            ),
        ),
        migrations.AlterField(
            model_name="adult",
            name="ethnic_group",
            field=models.ForeignKey(
                blank=True,
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="web.ethnicgroup",
            ),
        ),
        migrations.AlterField(
            model_name="adult",
            name="experience",
            field=models.ForeignKey(
                blank=True,
                help_text="Overall, how was your experience of our service?",
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="experience",
                to="web.rating",
            ),
        ),
        migrations.AlterField(
            model_name="adult",
            name="explaining",
            field=models.ForeignKey(
                blank=True,
                help_text="How good were our services at explaining information clearly?",
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="explaining",
                to="web.rating",
            ),
        ),
        migrations.AlterField(
            model_name="adult",
            name="gender",
            field=models.ForeignKey(
                blank=True,
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="web.gender",
            ),
        ),
        migrations.AlterField(
            model_name="adult",
            name="kind",
            field=models.ForeignKey(
                blank=True,
                help_text="How good were our services at being kind to you?",
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="kind",
                to="web.rating",
            ),
        ),
        migrations.AlterField(
            model_name="adult",
            name="listening",
            field=models.ForeignKey(
                blank=True,
                help_text="How good were our services at listening to you?",
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="listening",
                to="web.rating",
            ),
        ),
        migrations.AlterField(
            model_name="adult",
            name="positive",
            field=models.ForeignKey(
                blank=True,
                help_text="How good were our services at making a positive difference to your health and wellbeing?",
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="positive",
                to="web.rating",
            ),
        ),
        migrations.AlterField(
            model_name="adult",
            name="pregnant",
            field=models.ForeignKey(
                blank=True,
                help_text="Are you pregnant at this time?",
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="pregnant",
                to="web.pregnant",
            ),
        ),
        migrations.AlterField(
            model_name="adult",
            name="relationship",
            field=models.ForeignKey(
                blank=True,
                help_text="What is your relationship status?",
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="web.relationship",
            ),
        ),
        migrations.AlterField(
            model_name="adult",
            name="religion",
            field=models.ForeignKey(
                blank=True,
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="web.religion",
            ),
        ),
        migrations.AlterField(
            model_name="adult",
            name="sexual_orientation",
            field=models.ForeignKey(
                blank=True,
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="web.sexualorientation",
            ),
        ),
        migrations.AlterField(
            model_name="adult",
            name="treatment",
            field=models.ForeignKey(
                blank=True,
                help_text="How good were our services at involving you in decisions about your care or treatment?",
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="treatment",
                to="web.rating",
            ),
        ),
        migrations.AlterField(
            model_name="carer",
            name="age",
            field=models.ForeignKey(
                blank=True,
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="web.age",
            ),
        ),
        migrations.AlterField(
            model_name="carer",
            name="assessment",
            field=models.ForeignKey(
                blank=True,
                help_text="Did we tell you who to contact for a carers assessment?",
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="carer_assessment",
                to="web.contactgeneric",
            ),
        ),
        migrations.AlterField(
            model_name="carer",
            name="carer_type",
            field=models.ForeignKey(
                blank=True,
                help_text="I am a carer, family member, friend, parent or guardian of someone:",
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="carer_type",
                to="web.carertype",
            ),
        ),
        migrations.AlterField(
            model_name="carer",
            name="disability",
            field=models.ForeignKey(
                blank=True,
                help_text="Do you have a long term disability or a long-term health condition which affects your day to day activities?",
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="web.disability",
            ),
        ),
        migrations.AlterField(
            model_name="carer",
            name="ethnic_group",
            field=models.ForeignKey(
                blank=True,
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="web.ethnicgroup",
            ),
        ),
        migrations.AlterField(
            model_name="carer",
            name="experience",
            field=models.ForeignKey(
                blank=True,
                help_text="Overall, how was your experience of our service?",
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="carer_experience",
                to="web.rating",
            ),
        ),
        migrations.AlterField(
            model_name="carer",
            name="explaining",
            field=models.ForeignKey(
                blank=True,
                help_text="How good were our services at explaining information clearly?",
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="carer_explaining",
                to="web.rating",
            ),
        ),
        migrations.AlterField(
            model_name="carer",
            name="gender",
            field=models.ForeignKey(
                blank=True,
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="web.gender",
            ),
        ),
        migrations.AlterField(
            model_name="carer",
            name="kind",
            field=models.ForeignKey(
                blank=True,
                help_text="How good were our services at being kind to you?",
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="carer_kind",
                to="web.rating",
            ),
        ),
        migrations.AlterField(
            model_name="carer",
            name="listening",
            field=models.ForeignKey(
                blank=True,
                help_text="How good were our services at listening to you?",
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="carer_listening",
                to="web.rating",
            ),
        ),
        migrations.AlterField(
            model_name="carer",
            name="relationship",
            field=models.ForeignKey(
                blank=True,
                help_text="What is your relationship status?",
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="web.relationship",
            ),
        ),
        migrations.AlterField(
            model_name="carer",
            name="religion",
            field=models.ForeignKey(
                blank=True,
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="web.religion",
            ),
        ),
        migrations.AlterField(
            model_name="carer",
            name="sexual_orientation",
            field=models.ForeignKey(
                blank=True,
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="web.sexualorientation",
            ),
        ),
        migrations.AlterField(
            model_name="carer",
            name="treatment",
            field=models.ForeignKey(
                blank=True,
                help_text="How good were our services at involving you in decisions about the care and treatment of the person you care for?",
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="carer_treatment",
                to="web.rating",
            ),
        ),
        migrations.AlterField(
            model_name="carer",
            name="worried",
            field=models.ForeignKey(
                blank=True,
                help_text="Did our services tell you who you could contact if you were worried about the person you care for?",
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="carer_worried",
                to="web.contactgeneric",
            ),
        ),
        migrations.AlterField(
            model_name="child",
            name="age",
            field=models.ForeignKey(
                blank=True,
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="web.childage",
            ),
        ),
        migrations.AlterField(
            model_name="child",
            name="carer_type",
            field=models.ForeignKey(
                blank=True,
                help_text="I am a: ",
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="web.serviceuser",
            ),
        ),
        migrations.AlterField(
            model_name="child",
            name="disability",
            field=models.ForeignKey(
                blank=True,
                help_text="Do you have a long term disability or a long-term health condition which affects your day to day activities?",
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="web.disability",
            ),
        ),
        migrations.AlterField(
            model_name="child",
            name="ethnic_group",
            field=models.ForeignKey(
                blank=True,
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="web.ethnicgroup",
            ),
        ),
        migrations.AlterField(
            model_name="child",
            name="experience",
            field=models.ForeignKey(
                blank=True,
                help_text="Overall, how was your experience of our service?",
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="child_experience",
                to="web.rating",
            ),
        ),
        migrations.AlterField(
            model_name="child",
            name="explaining",
            field=models.ForeignKey(
                blank=True,
                help_text="How good were our services at explaining information clearly?",
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="child_explaining",
                to="web.childrating",
            ),
        ),
        migrations.AlterField(
            model_name="child",
            name="gender",
            field=models.ForeignKey(
                blank=True,
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="web.gender",
            ),
        ),
        migrations.AlterField(
            model_name="child",
            name="kind",
            field=models.ForeignKey(
                blank=True,
                help_text="How good were our services at being kind to you?",
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="child_kind",
                to="web.childrating",
            ),
        ),
        migrations.AlterField(
            model_name="child",
            name="listening",
            field=models.ForeignKey(
                blank=True,
                help_text="How good were our services at listening to you?",
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="child_listening",
                to="web.childrating",
            ),
        ),
        migrations.AlterField(
            model_name="child",
            name="positive",
            field=models.ForeignKey(
                blank=True,
                help_text="How good were our services at making a positive difference to your health and wellbeing?",
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="child_positive",
                to="web.childrating",
            ),
        ),
        migrations.AlterField(
            model_name="child",
            name="relationship",
            field=models.ForeignKey(
                blank=True,
                help_text="What is your relationship status?",
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="web.relationship",
            ),
        ),
        migrations.AlterField(
            model_name="child",
            name="religion",
            field=models.ForeignKey(
                blank=True,
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="web.religion",
            ),
        ),
        migrations.AlterField(
            model_name="child",
            name="sexual_orientation",
            field=models.ForeignKey(
                blank=True,
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="web.sexualorientation",
            ),
        ),
        migrations.AlterField(
            model_name="child",
            name="treatment",
            field=models.ForeignKey(
                blank=True,
                help_text="How good were our services at involving you in decisions about your care or treatment?",
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="child_treatment",
                to="web.childrating",
            ),
        ),
        migrations.AlterField(
            model_name="youngcarer",
            name="age",
            field=models.ForeignKey(
                blank=True,
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="web.childage",
            ),
        ),
        migrations.AlterField(
            model_name="youngcarer",
            name="assessment",
            field=models.ForeignKey(
                blank=True,
                help_text="Did we tell you who to contact for a carers assessment?",
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="young_carer_assessment",
                to="web.childrating",
            ),
        ),
        migrations.AlterField(
            model_name="youngcarer",
            name="disability",
            field=models.ForeignKey(
                blank=True,
                help_text="Do you have a long term disability or a long-term health condition which affects your day to day activities?",
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="web.disability",
            ),
        ),
        migrations.AlterField(
            model_name="youngcarer",
            name="ethnic_group",
            field=models.ForeignKey(
                blank=True,
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="web.ethnicgroup",
            ),
        ),
        migrations.AlterField(
            model_name="youngcarer",
            name="experience",
            field=models.ForeignKey(
                blank=True,
                help_text="Overall, how was your experience of our service?",
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="young_carer_experience",
                to="web.rating",
            ),
        ),
        migrations.AlterField(
            model_name="youngcarer",
            name="explaining",
            field=models.ForeignKey(
                blank=True,
                help_text="Were our services good at explaining things clearly?",
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="young_carer_explaining",
                to="web.childrating",
            ),
        ),
        migrations.AlterField(
            model_name="youngcarer",
            name="gender",
            field=models.ForeignKey(
                blank=True,
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="web.gender",
            ),
        ),
        migrations.AlterField(
            model_name="youngcarer",
            name="involving",
            field=models.ForeignKey(
                blank=True,
                help_text="Were our services good at involving you in the way we helped the person you care for?",
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="young_carer_involving",
                to="web.childrating",
            ),
        ),
        migrations.AlterField(
            model_name="youngcarer",
            name="kind",
            field=models.ForeignKey(
                blank=True,
                help_text="Were our services good at being kind to you?",
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="young_carer_kind",
                to="web.childrating",
            ),
        ),
        migrations.AlterField(
            model_name="youngcarer",
            name="listening",
            field=models.ForeignKey(
                blank=True,
                help_text="Were our services good at listening to you?",
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="young_carer_listening",
                to="web.childrating",
            ),
        ),
        migrations.AlterField(
            model_name="youngcarer",
            name="relationship",
            field=models.ForeignKey(
                blank=True,
                help_text="What is your relationship status?",
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="web.relationship",
            ),
        ),
        migrations.AlterField(
            model_name="youngcarer",
            name="religion",
            field=models.ForeignKey(
                blank=True,
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="web.religion",
            ),
        ),
        migrations.AlterField(
            model_name="youngcarer",
            name="sexual_orientation",
            field=models.ForeignKey(
                blank=True,
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="web.sexualorientation",
            ),
        ),
        migrations.AlterField(
            model_name="youngcarer",
            name="talking",
            field=models.ForeignKey(
                blank=True,
                help_text="Were our services good at talking to you about the support you could have as a carer?",
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="young_carer_talking",
                to="web.childrating",
            ),
        ),
        migrations.AlterField(
            model_name="youngcarer",
            name="worried",
            field=models.ForeignKey(
                blank=True,
                help_text="Did our services tell you who you could contact if you were worried about the person you care for?",
                limit_choices_to={"hidden": False},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="young_carer_worried",
                to="web.childrating",
            ),
        ),
    ]
