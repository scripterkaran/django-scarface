# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scarface', '0004_auto_20151217_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='pushmessage',
            name='image',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='pushmessage',
            name='picture',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='pushmessage',
            name='style',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='pushmessage',
            name='summaryText',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='pushmessage',
            name='title',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
