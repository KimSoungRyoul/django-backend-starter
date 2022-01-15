# Generated by Django 3.2.6 on 2021-09-22 11:07
import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("study_example_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Team",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=32)),
            ],
        ),
        migrations.AlterField(
            model_name="student",
            name="major",
            field=models.CharField(default="sdf", help_text="전공", max_length=34),
        ),
        migrations.AddField(
            model_name="student",
            name="team",
            field=models.ForeignKey(
                help_text="sdfsdf2222",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="study_example_app.team",
            ),
        ),
    ]