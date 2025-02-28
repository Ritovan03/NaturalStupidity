# Generated by Django 4.0.4 on 2022-05-23 07:14

import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("documents", "1021_webp_thumbnail_conversion"),
    ]

    operations = [
        migrations.CreateModel(
            name="PaperlessTask",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("task_id", models.CharField(max_length=128)),
                ("name", models.CharField(max_length=256, null=True)),
                (
                    "created",
                    models.DateTimeField(auto_now=True, verbose_name="created"),
                ),
                (
                    "started",
                    models.DateTimeField(null=True, verbose_name="started"),
                ),
                ("acknowledged", models.BooleanField(default=False)),
                (
                    "attempted_task",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="attempted_task",
                        # This is a dummy field, 1026 will fix up the column
                        # This manual change is required, as django doesn't django doesn't really support
                        # removing an app which has migration deps like this
                        to="documents.document",
                    ),
                ),
            ],
        ),
    ]
