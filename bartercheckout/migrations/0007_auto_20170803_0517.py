# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-03 05:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bartercheckout', '0006_auto_20170803_0510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barterevent',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
