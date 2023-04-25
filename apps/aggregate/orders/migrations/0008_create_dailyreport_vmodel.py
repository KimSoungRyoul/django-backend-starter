# Generated by Django 4.1.4 on 2022-12-11 08:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('orders', '0006_auto_20211017_0925'),
    ]

    operations = [
        migrations.RunSQL(
            state_operations=[
                migrations.CreateModel(
                    name='DailyReportVModel',
                    fields=[
                        ('day', models.DateField(help_text='날짜', primary_key=True, serialize=False)),
                        ('total_sales', models.IntegerField(help_text='일 주문 총 매출')),
                        ('total_cnt', models.IntegerField(help_text='일 주문 총 갯수')),
                    ],
                    options={
                        'db_table': 'daily_report_view_table',
                    },
                ),
            ],

            sql="""
            create view daily_report_view_table as
                SELECT DATE_TRUNC('day', O.created_at) AS day,
                     COUNT(*) AS total_cnt,
                     SUM(O.total_price) as total_sales
                FROM orders_order O
                group by DATE_TRUNC('day', O.created_at);
            comment on view daily_report_view_table is '주문 일별통계 뷰테이블(vtable)입니다';
            """,
            reverse_sql="""drop view daily_report_view_table;"""

        )

    ]
