# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-10 14:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='features',
            field=models.BooleanField(default=False),
        ),
    ]
