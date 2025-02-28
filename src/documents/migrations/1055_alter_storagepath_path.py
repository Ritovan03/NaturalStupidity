# Generated by Django 5.1.1 on 2024-10-03 14:47

from django.conf import settings
from django.db import migrations
from django.db import models
from django.db import transaction
from filelock import FileLock

from documents.templating.utils import convert_format_str_to_template_format


def convert_from_format_to_template(apps, schema_editor):
    StoragePath = apps.get_model("documents", "StoragePath")

    with transaction.atomic(), FileLock(settings.MEDIA_LOCK):
        for storage_path in StoragePath.objects.all():
            storage_path.path = convert_format_str_to_template_format(storage_path.path)
            storage_path.save()


class Migration(migrations.Migration):
    dependencies = [
        ("documents", "1054_customfieldinstance_value_monetary_amount_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="storagepath",
            name="path",
            field=models.TextField(verbose_name="path"),
        ),
        migrations.RunPython(
            convert_from_format_to_template,
            migrations.RunPython.noop,
        ),
    ]
