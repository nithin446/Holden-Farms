# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 02:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainForm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PigEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('number_pigs', models.IntegerField()),
                ('room_num', models.IntegerField()),
                ('farm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
