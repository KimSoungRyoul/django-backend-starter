# Generated by Django 3.2.6 on 2021-09-22 12:18
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='aa',
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, help_text='전화번호', max_length=64),
        ),
    ]
