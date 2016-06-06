# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 09:09
from __future__ import unicode_literals

from django.db import migrations, models
import shangcheng.models


class Migration(migrations.Migration):

    dependencies = [
        ('shangcheng', '0009_auto_20160520_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img_thum',
            field=models.ImageField(blank=True, height_field=50, null=True, upload_to=shangcheng.models.ThumPathAndRename('product/thum/'), verbose_name='缩略图', width_field=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='img_detail_1',
            field=models.ImageField(blank=True, null=True, upload_to=shangcheng.models.PathAndRename('product/'), verbose_name='详情图片地址1'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img_detail_2',
            field=models.ImageField(blank=True, null=True, upload_to=shangcheng.models.PathAndRename('product/'), verbose_name='详情图片地址2'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img_detail_3',
            field=models.ImageField(blank=True, null=True, upload_to=shangcheng.models.PathAndRename('product/'), verbose_name='详情图片地址3'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img_show',
            field=models.ImageField(blank=True, null=True, upload_to=shangcheng.models.PathAndRename('product/'), verbose_name='展示图片地址'),
        ),
    ]
