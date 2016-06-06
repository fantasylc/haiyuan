# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 07:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shangcheng', '0006_auto_20160520_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 5, 20, 7, 5, 9, 22429, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('0', '采购中'), ('1', '上线')], default='', max_length=5, verbose_name='状态'),
        ),
    ]
