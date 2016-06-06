# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-04 14:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shangcheng', '0013_product_unit'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(default='', verbose_name='关于我们')),
            ],
            options={
                'verbose_name': '关于我们',
                'verbose_name_plural': '关于我们',
            },
        ),
        migrations.CreateModel(
            name='Cartitem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, verbose_name='数量')),
                ('sum_price', models.FloatField(default=0.0, verbose_name='小计')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '购物车头目',
                'verbose_name_plural': '购物车头目',
                'ordering': ['date_added'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(default='', max_length=80, verbose_name='Token')),
                ('date_add', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('total_money', models.FloatField(default=0.0, verbose_name='总价')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='拥有者')),
            ],
            options={
                'verbose_name': '订单',
                'verbose_name_plural': '订单',
            },
        ),
        migrations.CreateModel(
            name='TopProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='顶级分类名')),
                ('index', models.IntegerField(default=1, verbose_name='排序')),
            ],
            options={
                'verbose_name': '商品顶级分类',
                'verbose_name_plural': '商品顶级分类',
                'ordering': ['index', 'name'],
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('1', '上线'), ('0', '采购中')], default='', max_length=5, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='parent',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='childs', to='shangcheng.TopProductCategory', verbose_name='顶级分类'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='order',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='shangcheng.Order', verbose_name='条目'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car', to='shangcheng.Product', verbose_name='商品'),
        ),
    ]
