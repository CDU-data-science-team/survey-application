# Generated by Django 4.0.5 on 2022-06-28 10:46

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CommentsCode",
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
        migrations.AddField(
            model_name="person",
            name="criticality",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="person",
            name="positivity",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="person",
            name="best_code_1",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="best1",
                to="web.commentscode",
            ),
        ),
        migrations.AddField(
            model_name="person",
            name="best_code_2",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="best2",
                to="web.commentscode",
            ),
        ),
        migrations.AddField(
            model_name="person",
            name="improve_code_1",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="improve1",
                to="web.commentscode",
            ),
        ),
        migrations.AddField(
            model_name="person",
            name="improve_code_2",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="improve2",
                to="web.commentscode",
            ),
        ),
    ]
