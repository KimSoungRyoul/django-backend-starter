# Generated by Django 3.1.4 on 2021-08-06 02:14
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('study_example_app', '0002_exampleuser_aaa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exampleuser',
            name='aaa',
            field=models.CharField(default='dd22', max_length=33),
        ),
    ]
