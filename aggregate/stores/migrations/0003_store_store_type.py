# Generated by Django 3.2.6 on 2021-08-22 10:09
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_store_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='store_type',
            field=models.CharField(choices=[('food', '배달음식'), ('grocery', '식료품/가공식품'), ('pet_food', '반려동물음식')], default='food', help_text='상점 유형', max_length=32),
            preserve_default=False,
        ),
    ]
