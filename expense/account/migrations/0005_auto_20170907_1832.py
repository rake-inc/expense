# -*- coding: utf-8 -*-
# Generated by Django 1.11a1 on 2017-09-07 18:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20170907_1555'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserMod',
        ),
        migrations.AlterField(
            model_name='expensedetails',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
    ]
