# Generated by Django 3.1.4 on 2021-07-25 05:50
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='aa',
            field=models.CharField(default='aa', max_length=64),
            preserve_default=False,
        ),
    ]
