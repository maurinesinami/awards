# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-01 04:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('award', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='image_caption',
            new_name='image_description',
        ),
        migrations.AddField(
            model_name='image',
            name='live_link',
            field=models.CharField(default=2, max_length=30),
            preserve_default=False,
        ),
    ]