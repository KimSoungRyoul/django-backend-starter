# Generated by Django 4.0.3 on 2022-05-21 07:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0006_customer_storeowner"),
    ]

    operations = [
        migrations.CreateModel(
            name="Organization",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=32)),
            ],
        ),
    ]
