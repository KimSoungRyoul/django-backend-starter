# Generated by Django 4.2 on 2023-04-23 07:07

import django.contrib.auth.models
import django.db.models.deletion
import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0009_insert_init_organization_data"),
    ]

    operations = [
        migrations.CreateModel(
            name="Department",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("parent1_name", models.CharField(db_comment="최상위 소속 부서명", max_length=32)),
                ("parent2_name", models.CharField(db_comment="중간 소속 부서명", max_length=32)),
                ("parent3_name", models.CharField(db_comment="상세 소속 부서명", max_length=32)),
            ],
            options={
                "db_table": "department",
            },
        ),
        migrations.CreateModel(
            name="Staff",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("users.user",),
            managers=[
                ("objects", django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name="user",
            name="user_type",
            field=models.CharField(
                choices=[("customer", "고객"), ("store_owner", "사장님"), ("staff", "직원")],
                default="customer",
                help_text="고객 유형",
                max_length=16,
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="department",
            field=models.ForeignKey(
                db_comment="소속부서", null=True, on_delete=django.db.models.deletion.CASCADE, to="users.department"
            ),
        ),
    ]
