# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-20 20:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0007_gallery_total_rankers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gallery',
            old_name='rank',
            new_name='rating',
        ),
        migrations.RenameField(
            model_name='gallery',
            old_name='total_rankers',
            new_name='total_raters',
        ),
    ]
