# Generated by Django 4.1.3 on 2022-11-16 15:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0007_organization"),
    ]

    operations = [
        migrations.AlterField(
            model_name="organization",
            name="name",
            field=models.CharField(db_column="org_name", max_length=32),
        ),
    ]
