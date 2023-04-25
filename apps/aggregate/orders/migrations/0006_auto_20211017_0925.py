# Generated by Django 3.2.6 on 2021-10-17 09:25
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0005_alter_order_status"),
    ]

    operations = [
        migrations.CreateModel(
            name="DailyReport",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("order_total_cnt", models.IntegerField()),
            ],
            options={
                "managed": False,
            },
        ),
        migrations.AddField(
            model_name="order",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, help_text="주문이 생성된 시간"),
            preserve_default=False,
        ),
    ]
