# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-15 05:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_profile_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='posts.Project'),
        ),
    ]