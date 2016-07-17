# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-17 22:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0002_artpiece_artist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='artpiece',
            name='gallery',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='showcase.Gallery'),
        ),
    ]