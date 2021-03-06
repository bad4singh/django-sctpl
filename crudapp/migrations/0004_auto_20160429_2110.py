# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-29 21:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0003_delete_nameform'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='author',
            field=models.CharField(default=datetime.datetime(2016, 4, 29, 21, 10, 9, 218134, tzinfo=utc), max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='members',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 29, 21, 10, 31, 802426, tzinfo=utc), verbose_name='date published'),
            preserve_default=False,
        ),
    ]
