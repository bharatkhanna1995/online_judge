# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-20 11:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0007_auto_20160620_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_default_info',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
