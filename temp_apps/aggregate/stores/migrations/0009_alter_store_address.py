# Generated by Django 3.2.9 on 2021-12-26 03:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("stores", "0008_rename_text_storetext_contents"),
    ]

    operations = [
        migrations.AlterField(
            model_name="store",
            name="address",
            field=models.OneToOneField(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="stores.storeaddress"
            ),
        ),
    ]