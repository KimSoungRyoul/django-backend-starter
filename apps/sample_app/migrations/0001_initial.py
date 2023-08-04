# Generated by Django 4.2.3 on 2023-08-02 17:15

import django.contrib.postgres.indexes
from django.db import migrations, models
import django.db.models.deletion
import sample_app.models.order


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DailyReport",
            fields=[
                ("day", models.DateField(help_text="날짜", primary_key=True, serialize=False)),
                ("total_sales", models.IntegerField(help_text="일 주문 총 매출")),
                ("total_cnt", models.IntegerField(help_text="일 주문 총 갯수")),
            ],
            options={
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("waiting", "주문 수락 대기중"),
                            ("accepted", "주문 접수 완료"),
                            ("rejected", "주문 거절"),
                            ("delivery complete", "배달 완료"),
                        ],
                        db_comment="주문 상태값",
                        default="waiting",
                        max_length=32,
                    ),
                ),
                ("total_price", models.IntegerField(default=0)),
                ("created_at", models.DateTimeField(auto_now_add=True, help_text="주문이 생성된 시간")),
                ("address", models.JSONField(default=sample_app.models.order.default_address, help_text="주문 배송지")),
            ],
        ),
        migrations.CreateModel(
            name="OrderedProduct",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("count", models.IntegerField(db_comment="주문한 해당 메뉴의 갯수", default=1)),
            ],
            options={
                "db_table": "ordered_product",
                "db_table_comment": "주문된 상품, Order와 Product사이 매핑테이블",
            },
        ),
        migrations.CreateModel(
            name="OrderHistory",
            fields=[
                (
                    "order_number_pk",
                    models.CharField(help_text="파티션 키", max_length=512, primary_key=True, serialize=False),
                ),
                ("status", models.CharField(default="WAIT_FOR_ACCEPT", help_text="주문이력 기록당시 주문상태값", max_length=32)),
            ],
            options={
                "db_table": "pycon2023_order_history_table",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(db_comment="상품명", max_length=128)),
                ("price", models.PositiveIntegerField(db_comment="상품 가격")),
                ("created_at", models.DateTimeField(auto_now_add=True, db_comment="생성시간")),
                ("updated_at", models.DateTimeField(auto_now=True, db_comment="수정시간")),
                (
                    "product_type",
                    models.CharField(
                        choices=[("grocery", "식료품"), ("furniture", "가구"), ("books", "책"), ("food", "음식")], max_length=32
                    ),
                ),
            ],
            options={
                "db_table": "product",
                "db_table_comment": "상품 테이블 입니다.",
                "ordering": ("-created_at",),
                "indexes": [
                    models.Index(fields=["created_at"], name="created_at_index"),
                    django.contrib.postgres.indexes.HashIndex(fields=["name"], name="name_pt_composite_index"),
                ],
            },
        ),
        migrations.AddConstraint(
            model_name="product",
            constraint=models.UniqueConstraint(fields=("name", "product_type"), name="unique_product_name_type"),
        ),
        migrations.AddConstraint(
            model_name="product",
            constraint=models.CheckConstraint(
                check=models.Q(("price__lte", 100000000)), name="check_unreasonalbe_price"
            ),
        ),
        migrations.AddField(
            model_name="orderedproduct",
            name="order",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="sample_app.order"),
        ),
        migrations.AddField(
            model_name="orderedproduct",
            name="product",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="sample_app.product"),
        ),
        migrations.AddField(
            model_name="order",
            name="product_set",
            field=models.ManyToManyField(through="sample_app.OrderedProduct", to="sample_app.product"),
        ),
    ]
