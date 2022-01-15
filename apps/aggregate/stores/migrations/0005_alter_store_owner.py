# Generated by Django 3.2.6 on 2021-08-22 10:09
import django.db.models.deletion
from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("stores", "0004_alter_store_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="store",
            name="owner",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]