# Generated by Django 3.2.6 on 2021-09-23 11:48
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0003_order_store"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[("waiting", "주문 수락 대기중"), ("accepted", "주문 접수 완료"), ("delivery complete", "배달 완료")],
                default="waiting",
                help_text="주문 상태값",
                max_length=32,
            ),
        ),
    ]