# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shangcheng', '0011_auto_20160520_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('0', '采购中'), ('1', '上线')], default='', max_length=5, verbose_name='状态'),
        ),
    ]