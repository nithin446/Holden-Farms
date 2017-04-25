# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-25 04:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainForm', '0007_remove_pigentry_flow'),
    ]

    operations = [
        migrations.AddField(
            model_name='pigentry',
            name='flow',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainForm.Flow'),
        ),
        migrations.AlterField(
            model_name='flow',
            name='abbreviation',
            field=models.CharField(default='aaa', max_length=5),
        ),
        migrations.AlterField(
            model_name='flow',
            name='name',
            field=models.CharField(default='aaa', max_length=100),
        ),
    ]
