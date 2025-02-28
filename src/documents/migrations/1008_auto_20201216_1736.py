# Generated by Django 3.1.4 on 2020-12-16 17:36

import django.db.models.functions.text
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("documents", "1007_savedview_savedviewfilterrule"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="correspondent",
            options={"ordering": (django.db.models.functions.text.Lower("name"),)},
        ),
        migrations.AlterModelOptions(
            name="document",
            options={"ordering": ("-created",)},
        ),
        migrations.AlterModelOptions(
            name="documenttype",
            options={"ordering": (django.db.models.functions.text.Lower("name"),)},
        ),
        migrations.AlterModelOptions(
            name="savedview",
            options={"ordering": (django.db.models.functions.text.Lower("name"),)},
        ),
        migrations.AlterModelOptions(
            name="tag",
            options={"ordering": (django.db.models.functions.text.Lower("name"),)},
        ),
    ]
