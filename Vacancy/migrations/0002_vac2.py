# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 19:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vacancy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vac2',
            fields=[
                ('gsm_id', models.IntegerField(primary_key=True, serialize=False)),
                ('parking_id', models.IntegerField()),
                ('vacancy', models.IntegerField()),
            ],
        ),
    ]
