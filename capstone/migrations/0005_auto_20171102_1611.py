# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-02 16:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0004_auto_20171029_0520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='pubID',
            field=models.BigIntegerField(default=12345678, primary_key=True, serialize=False),
        ),
    ]
