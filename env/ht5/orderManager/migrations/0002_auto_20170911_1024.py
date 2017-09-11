# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-11 16:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderManager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='recipe_guid',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='client',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='order_guid',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='product_guid',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
