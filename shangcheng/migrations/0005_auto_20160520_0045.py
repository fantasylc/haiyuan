# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-19 16:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shangcheng', '0004_auto_20160520_0039'),
    ]

    operations = [
        migrations.RenameField(
            model_name='version',
            old_name='now_prize',
            new_name='now_price',
        ),
        migrations.RenameField(
            model_name='version',
            old_name='old_prize',
            new_name='old_price',
        ),
    ]