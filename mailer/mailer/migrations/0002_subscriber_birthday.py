# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-01-31 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='birthday',
            field=models.DateField(null=True, verbose_name=b'birthday'),
        ),
    ]